import logging
from http.server import BaseHTTPRequestHandler
from http.server import ThreadingHTTPServer
from urllib.parse import parse_qs
from settings import LOG_FILE, HOST, PORT


# ----------------- Logging Setup -----------------
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger("server")

def log_both(message):
    """Log to both terminal and log file."""
    print(message)
    logger.info(message)

# ----------------- Math Functions -----------------
def factorial(n: int) -> int:
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    if n < 0:
        raise ValueError("Input must be non-negative.")
    if n == 0 or n == 1:
        return 1

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def is_prime(n: int) -> bool:
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# ----------------- HTML Page -----------------
HTML_TEMPLATE = """\
<!DOCTYPE html>
<html>
<head>
    <title>Simple Math Server</title>
    <style>
        body {{ font-family: Arial; padding: 2em; }}
        form {{ margin-bottom: 1em; }}
        .result {{ margin-top: 1em; font-weight: bold; }}
    </style>
</head>
<body>
    <h1>Simple Math Web Server</h1>
    <form method="POST">
        <label><input type="radio" name="operation" value="factorial" {factorial_checked}> Factorial</label>
        <label><input type="radio" name="operation" value="is_prime" {prime_checked}> Is Prime</label><br><br>

        <label>Enter number:
            <input type="number" name="number" required>
        </label><br><br>

        <button type="submit">Compute</button>
    </form>
    {result_block}
</body>
</html>
"""

# ----------------- HTTP Handler -----------------
class SimpleMathHandler(BaseHTTPRequestHandler):
    def log_request_info(self, extra=""):
        log_both(f"{self.client_address[0]} {self.command} {self.path} {extra}")

    def do_GET(self):
        self.log_request_info()
        self.respond(self.render_page())

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length).decode()
        data = parse_qs(body)

        op = data.get("operation", ["factorial"])[0]
        num_str = data.get("number", ["0"])[0]

        self.log_request_info(f"POST data: operation={op}, number={num_str}")

        result_block = ""
        try:
            n = int(num_str)
            if op == "factorial":
                result_block = f"<div class='result'>Factorial of {n} is {factorial(n)}</div>"
            elif op == "is_prime":
                result_block = f"<div class='result'>Is {n} prime? {'Yes' if is_prime(n) else 'No'}</div>"
        except Exception as e:
            error_msg = f"Error processing request: {e}"
            log_both(error_msg)
            result_block = f"<div class='result' style='color:red;'>Error: {e}</div>"

        self.respond(self.render_page(op, result_block))

    def render_page(self, op="factorial", result_block=""):
        return HTML_TEMPLATE.format(
            factorial_checked="checked" if op == "factorial" else "",
            prime_checked="checked" if op == "is_prime" else "",
            result_block=result_block
        ).encode()

    def respond(self, content: bytes):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)

    def log_message(self, format, *args):
        # Override default BaseHTTPRequestHandler logging
        logger.info("%s - %s" % (self.address_string(), format % args))


# ----------------- Server Entry -----------------
if __name__ == "__main__":
    with ThreadingHTTPServer((HOST, PORT), SimpleMathHandler) as server:
        log_both(f"🚀 Server running at http://{HOST}:{PORT}")
        server.serve_forever()
