import time

import pytest

from rubrix.client.sdk.commons.errors import ForbiddenApiError


def test_delete_records_from_dataset(mocked_client):
    dataset = "test_delete_records_from_dataset"
    import rubrix as rb

    rb.delete(dataset)
    rb.log(
        name=dataset,
        records=[
            rb.TextClassificationRecord(
                id=i, text="This is the text", metadata=dict(idx=i)
            )
            for i in range(0, 50)
        ],
    )

    matched, processed = rb.delete_records(name=dataset, ids=[10], discard_only=True)
    assert matched, processed == (1, 1)

    ds = rb.load(name=dataset)
    assert len(ds) == 50

    time.sleep(1)
    matched, processed = rb.delete_records(
        name=dataset, query="id:10", discard_only=False
    )
    assert matched, processed == (1, 1)

    time.sleep(1)
    ds = rb.load(name=dataset)
    assert len(ds) == 49


def test_delete_records_without_permission(mocked_client):
    dataset = "test_delete_records_without_permission"
    import rubrix as rb

    rb.delete(dataset)
    rb.log(
        name=dataset,
        records=[
            rb.TextClassificationRecord(
                id=i, text="This is the text", metadata=dict(idx=i)
            )
            for i in range(0, 50)
        ],
    )
    try:
        mocked_client.change_current_user("mock-user")
        matched, processed = rb.delete_records(
            name=dataset, ids=[10], discard_only=True
        )
        assert matched, processed == (1, 1)

        with pytest.raises(ForbiddenApiError):
            rb.delete_records(
                name=dataset,
                query="id:10",
                discard_only=False,
                discard_when_forbidden=False,
            )

        matched, processed = rb.delete_records(
            name=dataset,
            query="id:10",
            discard_only=False,
            discard_when_forbidden=True,
        )
        assert matched, processed == (1, 1)
    finally:
        mocked_client.reset_default_user()


def test_delete_records_with_unmatched_records(mocked_client):
    dataset = "test_delete_records_with_unmatched_records"
    import rubrix as rb

    rb.delete(dataset)
    rb.log(
        name=dataset,
        records=[
            rb.TextClassificationRecord(
                id=i, text="This is the text", metadata=dict(idx=i)
            )
            for i in range(0, 50)
        ],
    )

    matched, processed = rb.delete_records(dataset, ids=["you-wont-find-me-here"])
    assert (matched, processed) == (0, 0)