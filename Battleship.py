import random
def ShipLogic(round, yourMap, yourHp, enemyHp, p1ShotSeq, p1PrevHit, storage):
    print_key_info(round, yourMap, yourHp, enemyHp, p1ShotSeq, p1PrevHit, storage)
    x = random.randint(1,10)
    y = random.randint(1,10)
    return [x,y], storage


def print_key_info(round, yourMap, yourHp, enemyHp, p1ShotSeq, p1PrevHit, storage):
    print(f"Round: {round}")
    print(f"Yourmap: {yourMap}")
    print(f"yourHp: {yourHp}")
    print(f"enemyHp: {enemyHp}")
    print(f"p1ShotSeq: {p1ShotSeq}")
    print(f"p1PrevHit: {p1PrevHit}")
    print(f"Storage: {storage}")