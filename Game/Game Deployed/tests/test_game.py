from brownie import Game, network, accounts, config

def getAccount():
    acc = accounts[0]
    return acc
    

def deploy():
    acc = getAccount()
    dep = Game.deploy({"from":acc})
    return dep


def testDeploy():
    acc = getAccount()
    dep = deploy()
    

def testPlay():
    acc = getAccount()
    dep = deploy()
    
    for i in range(7):
        dep.play({"from":accounts[i], "value": "2 ether"})
    