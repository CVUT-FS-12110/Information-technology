# Software Testing Example

Start the server:

```bash
python math_server.py
```

---

## Testing Overview

### 1. Unit Tests - Math Functions

Test the core math functions independently. The server does **not** need to be running.

```bash
python test_math_utils.py
```

---

### 2. Server Status Response Test

Verify that the server responds correctly to HTTP requests.

```bash
python test_server.py
```

---

### 3. Server Benchmark

Measure server performance under multiple requests.

```bash
python test_benchmark.py
```

---

### 4. Passive Testing - Log Analysis

Analyze server logs to extract statistics and incidents.

```bash
python test_passive.py
```

---

### 5. End-to-End Testing with Selenium

Simulate a user interacting with the web interface in a real browser.

```bash
python test_end-to-end.py
```
