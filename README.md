# CLEAVE_Docker

### Building Docker images:

Local Docker images can be built using the Makefile (requires Docker and Docker Buildx, see https://docs.docker.com/build/architecture/).
Note that we use multi-stage builds to make rebuilds faster, see https://docs.docker.com/build/building/multi-stage/; the `base` stage only needs to be built once.

To build for a specific architecture (e.g. ARM64):

```bash
$ make base-arm64
$ make cleave-arm64
```

To build all images and architectures:

```bash
$ make all
```
To rebuild images:

```bash
$ docker buildx rm multiarch
$ docker buildx create --name multiarch --use —bootstrap
$ docker buildx build --platform=linux/arm64,linux/amd64 -f ./Dockerfile --target cleave -t expeca/cleave:cleave .
```

For Accessing Testbed:
1. Select worker using https://expeca.proj.kth.se/inventory/#worker-nodes
2. Lease worker node from https://testbed.expeca.proj.kth.se/project/leases/


For errors in Python 3.8 Distutils installation-- sudo apt-get install python3.8-distutils
