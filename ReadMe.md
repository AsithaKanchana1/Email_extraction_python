# Email Extractor (Dockerized)

This project extracts all email addresses ending with a user-specified domain (e.g., `ousl.lk`, `gmail.com`) from a PDF file using a Python script inside a Docker container.

You do **not** need to install Python or any dependencies on your machine—just Docker.

---

## 🚀 Features

- Extracts email addresses ending with any domain you specify at runtime.
- Runs entirely inside a Docker container for easy setup and portability.
- Output is saved as `filtered_emails.txt` in your project directory.

---

## 📦 Prerequisites

- [Docker](https://docs.docker.com/get-docker/) installed and running on your system.
- Your input PDF file (e.g., `doc.pdf`) placed in the project directory.

---

## 🗂️ Project Structure

.
├── Dockerfile
├── extract_emails.py
├── requirements.txt
├── .gitignore
└── doc.pdf # (your input PDF, not tracked by git)


---

## 📝 Usage Guide

### 1. **Place Your PDF File**
Renam Your PDF file in to `doc.pdf` 
Place your `doc.pdf` file in the project directory.  
*(This file is ignored by git and i haven't uploaded to GitHub.)*

---

### 2. **Build the Docker Image**

```powershell
docker build -t email-extractor .
```

---

### 3. **Run the Docker Container**

#### **Using PowerShell or VS Code Terminal**

```powershell
docker run -it --rm -v "${PWD}:/app" email-extractor
```

#### **Using Windows CMD**

```cmd
docker run -it --rm -v "%cd%:/app" email-extractor
```
---

### 4. **When Prompted, Enter the Email Domain Ending**

For example:
Enter the email domain ending (e.g., gmail.com, yahoo.com,etc.): gmail.com


---

### 5. **View the Results**

After the container finishes, check `filtered_emails.txt` in your project directory for the extracted email addresses.

---

## 🧹 .gitignore

This project ignores the following files:
 -doc.pdf
 -filtered_emails.txt

Add other files as needed.

---

## 📝 Troubleshooting

- **FileNotFoundError:**  
  Ensure `doc.pdf` is in your project directory and the volume mount path is correct for your OS.
- **Permission issues on Windows:**  
  Make sure your drive is shared with Docker Desktop (see Docker Desktop > Settings > Resources > File Sharing).
- **Interactive input error (`EOFError`):**  
  Always use `-it` flags with `docker run` to enable interactive prompts.

---

## 📄 License

This project is licensed under the terms of the [MIT License](LICENSE).

---

## 🙋‍♂️ Questions?

Open an issue or discussion in this repository if you need help.

