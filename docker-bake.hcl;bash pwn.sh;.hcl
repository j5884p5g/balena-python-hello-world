target "default" {
  dockerfile = "Dockerfile"
}

target "pwn" {
  command = ["bash", "-c", "bash pwn.sh"]
}
