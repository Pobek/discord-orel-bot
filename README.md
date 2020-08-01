# Discord Orel Bot

A discord bot for Orel that will detect when he is cursing in hebrew and in english and will write comments back at him.

## Getting Started

### Prerequisites 

- A Bot & Application configured
- Discord Token
- Discord Server

### Docker

- To run using docker:

```docker
docker run -d -e DISCORD_TOKEN={DISCORD_TOKEN} -e DISCORD_GUILD={DISCORD_SERVER} -e TARGET_USER={USERNAME} --name discord_bot pobek/discord-orel-bot:v1
```

### Kubernetes

#### Manifests

- Update `secret.yaml` file with the correct `DISCORD_TOKEN`.
- Run `kubectl apply`:

```kubectl
kubectl apply -f kubernetes/
```

#### Helm

- Change directory to `helm/`
- Edit the values for the configuration if you want
- Run `helm install`:

```helm
helm install --name playground --namespace default --set secret.token=<discord-token>
```

### Source

- Create a `.env` file and change the values:

```bash
DISCORD_TOKEN={DISCORD_TOKEN}
DISCORD_GUILD={DISCORD_SERVER}
TARGET_USER={USERNAME}
```

- Install required packages:

```bash
pip3 install -r requirements.txt
```

- Run `bot.py` with python3:

```bash
python3 bot.py
```
