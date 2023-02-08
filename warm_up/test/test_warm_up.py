from unittest.mock import Mock, patch
import warm_up.src.warm_up


def test_returns_name_of_bucket_created():
    with patch('src.app.warm_up.s3') as mock:
        BUCKET = 'warm-up-bucket-cl'
        mock.create_bucket(Bucket=BUCKET)
        print(mock)

        assert mock.list_buckets()['Buckets'] == []
