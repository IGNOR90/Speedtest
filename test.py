import jsonimport subprocessimport logginglogging.basicConfig(filename='speedtest.log', filemode='a', level=logging.INFO)server_list = [37382, 46774, 10987, 6386]host_list = ['8.8.4.4', 'ya.ru', 'amazon.com']bot_token = '1178689163:AAGzuJ961up3kwxpPR_mNxlG7y9NWkSFG7g'def exec_process(command, args):    process = subprocess.Popen([command] + args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)    stdout, stderr = process.communicate()    if stderr:        logging.error(stderr)    if stderr:        logging.error(stderr)    return stdoutdef speed_test(server_id):    args = [        '--server-id', str(server_id),        '--format', 'json',    ]    stdout = exec_process('speedtest', args)    return json.loads(stdout.decode("utf-8"))def mtr_test(host, count=50):    args = [        host,        '-i', '0.2',        '--no-dns',        # COUNT        '-c', str(count),        # PACKETSIZE        '-s', str(1000),        '--json'    ]    stdout = exec_process('mtr', args)    return json.loads(stdout.decode("utf-8"))def main_speed_test():    # mtr test    # for host_ip in host_list:    #     # break  # Пока так    #     logging.info(f'Testing mtr to {host_ip}')    #     mtr_test_result = mtr_test(host_ip)    #     data = mtr_test_result_formatter(mtr_test_result)    #     print(data)    # for chat_id in chat_ids:    #     sendMessage(data, chat_id, 'HTML')    # speed test    data_set = {}    for server_id in server_list:        logging.info(f'Testing server id {server_id}')        speed_test_result = speed_test(server_id)        speed_test_result['tariff_name'] = 'tariff_name'        data_set[speed_test_result['server']['id']] = speed_test_result        print(data_set)    return json.dumps(data_set)print(main_speed_test)