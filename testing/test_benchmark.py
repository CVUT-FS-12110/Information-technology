import time
import statistics
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from settings import URL

N_REQUESTS = 200        # total number of requests
N_WORKERS = 20          # number of parallel threads

def send_request(i):
    """Send a POST request and measure response time."""
    start = time.perf_counter()
    payload = {
        "operation": "factorial" if i % 2 == 0 else "is_prime",
        "number": str((i % 15) + 1)
    }
    try:
        r = requests.post(URL + "/", data=payload, timeout=5)
        elapsed = time.perf_counter() - start
        return elapsed, r.status_code
    except Exception as e:
        return None, f"ERR: {e}"

def main():
    print(f"🚀 Benchmarking {N_REQUESTS} requests with {N_WORKERS} workers to {URL}")
    response_times = []
    errors = 0

    with ThreadPoolExecutor(max_workers=N_WORKERS) as executor:
        futures = [executor.submit(send_request, i) for i in range(N_REQUESTS)]
        for future in as_completed(futures):
            elapsed, status = future.result()
            if elapsed is not None and status == 200:
                response_times.append(elapsed)
            else:
                errors += 1
                print(f"❌ Error: {status}")

    if response_times:
        avg = statistics.mean(response_times)
        p95 = statistics.quantiles(response_times, n=100)[94]  # 95th percentile
        total = sum(response_times)
        print("\n📊 Benchmark Results")
        print(f"  Total successful requests: {len(response_times)} / {N_REQUESTS}")
        print(f"  Errors: {errors}")
        print(f"  Average time: {avg*1000:.2f} ms")
        print(f"  95th percentile: {p95*1000:.2f} ms")
        print(f"  Total time spent: {total:.2f} s")
    else:
        print("❌ No successful responses recorded.")

if __name__ == "__main__":
    main()
