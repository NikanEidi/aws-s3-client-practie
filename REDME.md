# AWS S3 Python Projects (Boto3 Client-Based)

This repository contains a collection of Python scripts demonstrating how to work with **Amazon S3** using the **low-level `boto3` client interface**.

> ⚠️ This project only covers the `client` version of `boto3`. A separate repository will be created for the `resource` (high-level) version.

---

## 📦 Project Features

- ✅ Create and validate S3 buckets
- ✅ Upload files (static and user-selected)
- ✅ Upload files into folders (prefixes)
- ✅ Set custom storage classes
- ✅ Check metadata, file size, and type
- ✅ Download files
- ✅ Generate pre-signed URLs for secure sharing
- ✅ List and search files using prefix
- ✅ Delete files or entire folder prefixes
- ✅ Move files between buckets
- ✅ Apply bucket policies and file-level permissions
- ✅ Enable and work with versioning
- ✅ Perform multipart uploads

---

## 🗂️ File Structure

| Script                          | Purpose                                             |
|---------------------------------|-----------------------------------------------------|
| `upload_file.py`                | Uploads a default file to S3                        |
| `upload_custom_file.py`         | Uploads a user-selected file                        |
| `upload_to_folder.py`           | Uploads files to a virtual folder (prefix)         |
| `upload_with_storage_class.py`  | Uploads file with a custom storage class           |
| `check_file_info.py`            | Checks file metadata, size, and type               |
| `download_file.py`              | Downloads a file from S3                           |
| `generate_presigned_url.py`     | Generates a secure download/upload link            |
| `list_files.py`                 | Lists all files in the bucket                      |
| `search_file_by_prefix.py`      | Searches files using a prefix                      |
| `delete_file.py`                | Deletes a single file from S3                      |
| `delete_all_in_prefix.py`       | Deletes all files inside a folder prefix           |
| `transfer_between_buckets.py`   | Moves files from one bucket to another             |
| `set_bucket_policy.py`          | Applies a bucket-wide policy                       |
| `set_file_permission.py`        | Sets permissions for individual files              |
| `multipart_upload.py`           | Uploads large files in parts                       |
| `versioning.py`                 | Demonstrates version control in S3                 |

---

## 🚀 Getting Started

### 1. Clone this repo

```bash
git clone https://github.com/NikanEidi/aws-s3-client-projects.git
cd aws-s3-client-projects
```

### 2. Create and activate virtual environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```
---

## 🧠 Notes

- All operations are done using `boto3.client()` — not `resource`.
- Bucket names must be **globally unique** and follow naming conventions.
- Avoid hardcoding secrets — always use `.env` or environment variables.
- This project uses `"ca-central-1"` as the default region.

---

## 📚 Learning Goals

This repo is part of a **Summer Certification Learning Plan** to master AWS by building real-world Python projects.

---
---

## 🔗 Related Projects

If you're looking for the **low-level client interface version**, check this out:  
👉 [AWS S3 Client Interface Repository](https://github.com/NikanEidi/aws-s3-resource-practie)

---

## 🧑‍💻 Author

**Nikan Eydi**  
GitHub: [@NikanEidi](https://github.com/NikanEidi)

---

## 📜 License

This project is licensed under the MIT License.
