"""
tests for amqpclient.

isort:skip_file
"""

import os.path
import pytest
import sys

from amqpclient import rx, tx  # SUT


def test_help_rx():
    sys.argv += '--help'.split()
    with pytest.raises(SystemExit):
        rx.main()


def test_help_tx():
    sys.argv += '--help'.split()
    with pytest.raises(SystemExit):
        tx.main()


def test_default(mocker):
    sys.argv[1:] = ['-c', os.path.join(os.path.dirname(__file__), 'amqp_rxrc')]
    args = rx.parse_args()
    mocker.patch('pika.BlockingConnection')
    rx.rx(args)
    sys.argv += ['my_key', 'hello world!']
    tx_args = tx.parse_args()
    tx.tx(tx_args)
