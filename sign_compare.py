import hashlib
import hmac

# 定义密钥和消息
secret = '123123123123'
message = '!111'

# 将密钥和消息编码为字节对象
encoded_secret = secret.encode()
encoded_message = message.encode()

# 计算HMAC
digest = hmac.new(encoded_secret, encoded_message, hashlib.sha256).hexdigest()

# 打印结果
print(digest)