# DevOps Automation Task

This repository demonstrates a simple DevOps pipeline that uses:

- A Python script to collect metrics (simulated) from a list of servers.
- An Ansible playbook to deploy Nginx and place a basic index.html file.
- A Jenkins declarative pipeline to tie everything together.

## Table of Contents

1. [Project Requirements](#project-requirements)
2. [Repository Structure](#repository-structure)
3. [Instructions](#instructions)
4. [Next Steps & Notes](#next-steps--notes)

---

## Project Requirements

- **Python 3.x**
- **Ansible** (Version 2.9+ recommended)
- **Jenkins** (or Jenkinsfile-compatible environment)

You can run these locally or within a test VM. The pipeline can be tested by pointing an actual Jenkins instance to this repository or by using Jenkins in Docker.

---

## Repository Structure

.
├─ README.md # This file
├─ servers.txt # List of server IPs or hostnames
├─ collect_metrics.py # Python script to simulate collecting CPU usage
├─ deploy_nginx.yml # Ansible playbook to install & configure Nginx
└─ Jenkinsfile # Declarative Jenkins pipeline

---

## Instructions

1. **Set Up Your Environment**

   - Make sure Python and Ansible are installed locally.
   - If you have a Jenkins server, configure it to pull from this repo.

2. **Configure Your Servers**

   - Update `servers.txt` with the correct IP addresses/hostnames of your target servers.
   - Ensure these servers can be reached from wherever you’re running the Python/Ansible commands.
   - If you want to mock or simulate, you can keep them as placeholder IPs.

3. **Edit and Run the Python Script** (`collect_metrics.py`)

   - Add logic to read `servers.txt`, generate fake CPU metrics, and output a JSON/dictionary.
   - Run it locally via `python collect_metrics.py`.

4. **Review and Update the Ansible Playbook** (`deploy_nginx.yml`)

   - Add/modify tasks to install Nginx, copy an index.html, and start the service.
   - You may need to configure an inventory referencing `servers.txt` or use Ansible dynamic inventory.
   - Test locally with `ansible-playbook deploy_nginx.yml -i <inventory>`.

5. **Set Up the Jenkins Pipeline** (`Jenkinsfile`)
   - In your Jenkins server, create a new pipeline job pointing to this repo.
   - Adjust any paths or steps as necessary.
   - Run the pipeline and verify the stages (Checkout, Collect Metrics, Deploy, Verification) all function.

---

## Next Steps & Notes

- **Error Handling**: Consider how your scripts and playbooks handle missing data or unreachable hosts.
- **Security**: If you connect to real servers, ensure you’re managing credentials securely (SSH keys, vaults, etc.).
- **Customization**: You can extend this pipeline to deploy additional services or integrate real tests for verification.

If you have any questions, feel free to reach out to the repository owner or consult the official documentation for Python, Ansible, and Jenkins.
