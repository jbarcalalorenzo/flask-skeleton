# Camara-API

Async API to handle data from Camara devices.

## Getting started

Install [docker](https://docs.docker.com/engine/installation/) and run:

```shell
docker-compose up
# docker-compose stop
```

Otherwise, for the standalone web service:

```shell
pip install -r requirements.txt
python app.py
```

Visit [http://localhost:5000](http://localhost:5000)

## Development

Create a new branch off the **develop** branch for features or fixes.

After making changes rebuild images and run the app:

```shell
docker-compose build
docker-compose run -p 5000:5000 web python app.py
# docker stop flaskapp_redis_1
```

## Tests

Standalone unit tests run with:

```shell
pip install pytest pytest-cov pytest-flask
pytest --cov=web/ --ignore=tests/integration tests
```

Integration and unit tests run with:

```shell
docker-compose -f test.yml -p ci build
docker-compose -f test.yml -p ci run test python -m pytest --cov=web/ tests
# docker stop ci_redis_1 ci_web_1
```

Commits tested via [travis-ci.org](https://travis-ci.org/brennv/flask-app). Test coverage reported to [codecov.io](https://codecov.io/gh/brennv/flask-app). Code quality reported via [codeclimate.com](https://codeclimate.com/github/brennv/flask-app). Requirements inspected with [requires.io](https://requires.io/github/brennv/flask-app/requirements).

After testing, submit a pull request to merge changes with **develop**.

## Automated builds and redeploys

[Docker images](https://hub.docker.com/r/brenn/flask-app/tags/) are automatically built from changes to repo branches and tags via [docker hub autobuilds](https://docs.docker.com/docker-hub/github/).

Using a cluster provisioned on [docker cloud](https://cloud.docker.com/), services are created as stacks from `stack/` to nodes tagged *infra* or *compute*. Setting stack option `autoredeploy: true` continuously redeploys new images built from recent commits.

Image tagging and deployment scheme:

- `camara-api:latest` follows the **master** branch and deploys to **production** at [http://camara-api.example.com](http://camara-api.beta.build)
- `camara-api:develop` follows the **develop** branch and deploys to **staging** at [http://staging.camara-api.example.com](http://staging.camara-api.beta.build)

*Note:* To create sites at subdomains using virtual hosts as shown in `stack/`, assumes domain records have been configured with:

- `CNAME` record `*` to `example.com.`
- `A` record `@` to the (floating) IP of the haproxy load balancer

## Monitoring, log aggregation and scaling

Agent containers by [sematext](https://github.com/sematext/sematext-agent-docker) deployed to each node. Alert thresholds trigger web hooks to scale services under load.

## Notifications

Updates and alerts pushed via Slack:

- github
- travis-ci
- docker
- sematext