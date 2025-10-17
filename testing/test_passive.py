import re
from collections import defaultdict, namedtuple
from datetime import datetime
from settings import URL, LOG_FILE


# === Patterns ===
LINE_RE = re.compile(r'^(?P<ts>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3})\s+\[.*?\]\s+(?P<msg>.*)$')
IP_RE = re.compile(r'\b\d{1,3}(?:\.\d{1,3}){3}\b')
INCIDENT_RE = re.compile(r'\b(Error|Exception|Traceback|ERR)\b', re.IGNORECASE)
START_RE = re.compile(r'Server running', re.IGNORECASE)

Incident = namedtuple("Incident", ["ts", "ip", "msg"])
Event = namedtuple("Event", ["ts", "ip", "msg"])


def parse_timestamp(ts_str):
    try:
        return datetime.strptime(ts_str, "%Y-%m-%d %H:%M:%S,%f")
    except Exception:
        return None


def get_ip(text):
    m = IP_RE.search(text)
    return m.group(0) if m else None


def parse_log(path):
    starts = []
    incidents = []
    requests_per_ip = defaultdict(int)
    timeline = []

    with open(path, "r", encoding="utf-8", errors="replace") as f:
        for line in f:
            m = LINE_RE.match(line.strip())
            if not m:
                continue
            ts = parse_timestamp(m.group("ts"))
            msg = m.group("msg")
            ip = get_ip(msg)

            if START_RE.search(msg):
                starts.append(ts)

            if INCIDENT_RE.search(msg):
                incidents.append(Incident(ts, ip, msg))

            if ip:
                requests_per_ip[ip] += 1
                timeline.append(Event(ts, ip, msg))

    return starts, incidents, requests_per_ip, timeline


def print_stats(starts, incidents, requests_per_ip, timeline):
    print("\n=== Passive Server Log Statistics ===\n")

    print("🟢 Server starts:")
    if starts:
        for s in starts:
            print(f"  - {s}")
    else:
        print("  (none)")

    print(f"\n🚨 Incidents found: {len(incidents)}")
    for inc in incidents:
        print(f"  - {inc.ts} | {inc.ip or '(no ip)'} | {inc.msg}")

    print(f"\n🌐 Unique addresses: {len(requests_per_ip)}")
    for ip, count in sorted(requests_per_ip.items(), key=lambda x: x[1], reverse=True):
        print(f"  - {ip:15} : {count} requests")

    if timeline:
        first = min(e.ts for e in timeline)
        last = max(e.ts for e in timeline)
        print(f"\n📈 Timeline: {len(timeline)} events from {first} to {last} "
              f"({(last - first).total_seconds():.1f} s span)")
    else:
        print("\n📈 Timeline: No events")


def main():
    starts, incidents, requests_per_ip, timeline = parse_log(LOG_FILE)
    print_stats(starts, incidents, requests_per_ip, timeline)


if __name__ == "__main__":
    main()
