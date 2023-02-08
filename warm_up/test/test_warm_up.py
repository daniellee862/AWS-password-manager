from unittest.mock import Mock, patch
import src.warm_up


def test_returns_name_of_bucket_created():
    with patch('src.warm_up.s3') as mock:
        BUCKET = 'warm-up-bucket-cl'
        mock.create_bucket(Bucket=BUCKET)
        print(mock)

        assert mock.list_buckets()['Buckets'] == []
