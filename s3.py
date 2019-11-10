import boto
import boto.s3.connection
access_key = 'AKIAXKK2VKOIJTGNHBUU'
secret_key = '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'

conn = boto.connect_s3(
        aws_access_key_id = access_key,
        aws_secret_access_key = secret_key,
        host = 'https://503238185872.signin.aws.amazon.com/console',
        #is_secure=False,               # uncomment if you are not using ssl
        calling_format = boto.s3.connection.OrdinaryCallingFormat(),
        )
for bucket in conn.get_all_buckets():
        print("{name}\t{created}".format(name = bucket.name,created = bucket.creation_date))