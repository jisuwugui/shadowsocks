from musdk import client
import db_transfer
import config


class MuApiTransfer(db_transfer.TransferBase):
    client = None

    def __init__(self):
        super(MuApiTransfer, self).__init__()
        self.pull_ok = False  # 记录是否已经拉出过数据
        self.port_uid_table = {}
        self.init_mu_client()

    def init_mu_client(self):
        mu_url = config.mu_uri
        mu_token = config.token
        node_id = config.node_id
        mu_client = client.Client(mu_url, node_id, mu_token)
        self.client = mu_client

    def pull_db_all_user(self):
        print("pull all users...")
        return self.pull_db_users()

    def pull_db_users(self):
        users = self.client.get_users_res()
        for user in users:
            self.port_uid_table[user['port']] = user['id']
        return users

    def update_all_user(self, dt_transfer):
        print('call update all user')
        print(dt_transfer)
        update_transfer = {}
        for id in dt_transfer.keys():
            transfer = dt_transfer[id]
            if transfer[0] + transfer[1] < 1024:
                continue
            update_transfer[id] = transfer
        return update_transfer
