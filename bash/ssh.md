# SSH Quick Guide

## 1. Generate SSH Key
Run this on **your local machine**:
```bash
ssh-keygen -t ed25519
```
- Press **Enter** to accept the default path.
- Optionally set a passphrase.

| Algorithm   | Typical Key Size | Security Level   | Speed       | Notes |
|-------------|------------------|------------------|------------|-------|
| **RSA**     | 2048–4096 bits   | Good, but older  | Slower     | Larger keys, slower handshakes |
| **ECDSA**   | 256–521 bits     | Strong           | Fast       | Some compatibility issues on older systems |
| **ED25519** | **256 bits**     | **Very strong**  | **Very fast** | Preferred modern default; small key size and high performance |

Remember: When you generate SSH keys, two keys are created – a public key and a private key.
- The public key can be safely shared (e.g., added to a server).
- The private key **must always remain secret** and never be shared with anyone.



## 2. Show Your Public Key
Use `cat` to display the public key:
```bash
cat ~/.ssh/id_ed25519.pub
```
- Copy the whole line and add it to the **server** in:
  ```
  ~/.ssh/authorized_keys
  ```


## 3. Connect to the Server
```bash
ssh user@server-ip
```
- First time, type `yes` to trust the server.
- If your SSH server uses a custom port, e.g., 2222:
  ```bash
  ssh -p 2222 user@server-ip
  ```


## 4. Copy Files With `scp`

- **Upload a file to the server:**
  ```bash
  scp myfile.txt user@server-ip:/home/user/
  ```

- **Download a file from the server:**
  ```bash
  scp user@server-ip:/home/user/myfile.txt .
  ```


## Summary of Commands
| Task | Command |
|------|----------|
| Generate key | `ssh-keygen -t ed25519` |
| Show public key | `cat ~/.ssh/id_ed25519.pub` |
| SSH login | `ssh user@server-ip` |
| Upload file | `scp file.txt user@server-ip:/path/` |
| Download file | `scp user@server-ip:/path/file.txt .` |
