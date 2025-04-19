Email Extract Python Script
Place doc.pdf in current working directory
re build docker container
```bash
docker build -t email-extractor .
```
run the container using Power shell or vs code terminal
```powershell
docker run --rm -v "${PWD}:/app" email-extractor
```
if you are using CMD
```cmd
docker run --rm -v "%cd%:/app" email-extractor
```