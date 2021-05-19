import pytest
import click

AAVE_ADDR='0x7d2768dE32b0b80b7a3454c06BdAc94A69DDc7A9'

def test_flash(accounts, interface, Exploit):
    attacker = accounts[0]
    aave = interface.Aave(AAVE_ADDR, owner=attacker)

    exploit = Exploit.deploy({'from': attacker})
    tokens = [] # TODO put tokens list
    amounts = [] # TODO put amounts list
    modes = [0 for _ in tokens]

    tx = aave.flashLoan(exploit, tokens, amounts, modes, exploit, b'', 0)
    tx.info()

    for token in tokens:
        token_contract = interface.ERC20(token)
        print('profit:', token_contract.balanceOf(attacker), token_contract.symbol())
