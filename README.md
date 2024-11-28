# Ansible Collection - johanekstroms.contentmirror

Documentation for the collection.

## Create local development environment

```bash
brew install python3
python3 -m pip install venv
virtualenv .venv -p python3.13
source .venv/bin/activate
python3 -m pip install -r requirements.txt
ansible-galaxy collection install -r requirements.yml

```

## Run local tests

```bash
molecule test
```

## Setup a local Sonar Nexus 3

```bash
docker volume create --name nexus-data
docker run -d -p 8081:8081 --name nexus -v nexus-data:/nexus-data sonatype/nexus3
```

## Playbook example

```yaml
---
- name: Local run contentmirror.raw role
  hosts: localhost
  connection: local
  gather_facts: true
  tasks:
    - name: 'Include raw'
      ansible.builtin.include_role:
        name: raw
      vars:
        raw_src: http://sourcesite:8080/testfil
        raw_dst: http://destinationsite:8081/testfil

```

## Inventory example

```yaml
---
all:
  hosts:
    localhost:
      raw_src: http://localhost:8080/testfil
      raw_dst: http://localhost:8081/testfil

```

run container:

    docker run -e ANSIBLE_INVENTORY='/inventory.yml' -v ./inventory.yml:/inventory.yml:ro johanekstroms.raw:v1.0.0

change the vars in the inventory.yml with the vars
