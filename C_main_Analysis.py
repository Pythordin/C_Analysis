import os
import glob

bot_func = {
    "attack_app_proxy":"attack_app.c",
    "attack_app_http":"attack_app.c",
    "attack_app_cfnull":"attack_app.c",
    "killer_init":"killer.c",
    "killer_kill":"killer.c",
    "killer_kill_by_port":"killer.c",
    "has_exe_access":"killer.c",
    "status_upx_check":"killer.c",
    "memory_scan_match":"killer.c",
    "mem_exists":"killer.c",
    "util_strlen":"util.c",
    "util_strncmp":"util.c",
    "util_strcmp":"util.c",
    "util_strcpy":"util.c",
    "util_memcpy":"util.c",
    "util_zero":"util.c",
    "util_atoi":"util.c",
    "*util_itoa":"util.c",
    "util_memsearch":"util.c",
    "util_stristr":"util.c",
    "util_local_addr":"util.c",
    "*util_fdgets":"util.c",
    "util_isupper":"util.c",
    "util_isalpha":"util.c",
    "util_isspace":"util.c",
    "util_isdigit":"util.c",
    "attack_init":"attack.c",
    "attack_kill_all":"attack.c",
    "attack_parse":"attack.c",
    "attack_start":"attack.c",
    "*attack_get_opt_str":"attack.c",
    "attack_get_opt_int":"attack.c",
    "attack_get_opt_ip":"attack.c",
    "add_attack":"attack.c",
    "free_opts":"attack.c",
    "resolv_domain_to_hostname":"resolv.c",
    "resolv_skip_name":"resolv.c",
    "*resolv_lookup":"resolv.c",
    "resolv_entries_free":"resolv.c",
    "checksum_generic":"checksum.c",
    "checksum_tcpudp":"checksum.c",
    "rand_init":"rand.c",
    "recv_strip_null":"scanner.c",
    "scanner_init":"scanner.c",
    "scanner_kill":"scanner.c",
    "setup_connection":"scanner.c",
    "get_random_ip":"scanner.c",
    "consume_iacs":"scanner.c",
    "consume_any_prompt":"scanner.c",
    "consume_user_prompt":"scanner.c",
    "consume_pass_prompt":"scanner.c",
    "consume_resp_prompt":"scanner.c",
    "add_auth_entry":"scanner.c",
    "*random_auth_entry":"scanner.c",
    "report_working":"scanner.c",
    "*deobf":"scanner.c",
    "can_consume":"scanner.c",
    "segv_handler":"main.c",
    "main":"main.c",
    "anti_gdb_entry":"main.c",
    "resolve_cnc_addr":"main.c",
    "establish_connection":"main.c",
    "teardown_connection":"main.c",
    "ensure_single_instance":"main.c",
    "unlock_tbl_if_nodebug":"main.c",
    "table_init":"table.c",
    "table_unlock_val":"table.c",
    "table_lock_val":"table.c",
    "*table_retrieve_val":"table.c",
    "add_entry":"table.c",
    "toggle_obf":"table.c",
    "attack_udp_generic":"attack_udp.c",
    "attack_udp_vse":"attack_udp.c",
    "attack_udp_dns":"attack_udp.c",
    "attack_udp_plain":"attack_udp.c",
    "get_dns_resolver":"attack_udp.c",
    "attack_gre_ip":"attack_gre.c",
    "attack_gre_eth":"attack_gre.c",
    "attack_tcp_syn":"attack_tcp.c",
    "attack_tcp_ack":"attack_tcp.c",
    "attack_tcp_stomp":"attack_tcp.c",
}
    

def readFile(filePath):
    with open(filePath, 'r') as file:
        print(filePath)
        for line_number, line in enumerate(file, start=1):
            for search_func, place in bot_func.items():
                if search_func in line:
                    print(f"{search_func}, {line_number} /{place}")
    print()


def open_c_files(folder_path):
    # フォルダー内のすべてのC言語ファイルのパスを取得
    c_files = glob.glob(os.path.join(folder_path, '*.c'))


    # 各C言語ファイルを開く
    for file_path in c_files:
        readFile(file_path)

if __name__ == "__main__":
    open_c_files("/home/iot/ドキュメント/Mirai-Source-Code/mirai/bot/")