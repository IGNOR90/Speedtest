# Speedtest
sudo apt-get install curl
curl -s https://packagecloud.io/install/repositories/ookla/speedtest-cli/script.deb.sh | sudo bash
sudo apt-get install speedtest

Обязательный первый запрос в ручную: speedtest --server-id 6386 --format json