import heapq


def min_mana_to_win(initial_boss_hp, boss_damage, hard_mode=False):
    # Priority queue stores tuples:
    # (mana_spent, player_hp, player_mana, boss_hp, 
    # shield_timer, poison_timer, recharge_timer)
    pq = [(0, 50, 500, initial_boss_hp, 0, 0, 0)]
    visited = set()

    while pq:
        mana_spent, hp, mana, boss_hp, shield, poison, recharge = heapq.heappop(pq)

        # --- 1. PLAYER TURN ---
        if hard_mode:
            hp -= 1
            if hp <= 0:
                continue

        # Apply active effects at the start of Player turn
        if shield > 0:
            shield -= 1
        if poison > 0:
            boss_hp -= 3
            poison -= 1
        if recharge > 0:
            mana += 101
            recharge -= 1

        if boss_hp <= 0:
            return mana_spent

        # Deduplicate state (include hard_mode context implicitly by search path)
        state = (hp, mana, boss_hp, shield, poison, recharge)
        if state in visited:
            continue
        visited.add(state)

        # Player casts a spell
        # (cost, instant_damage, instant_heal, shield_time, poison_time, recharge_time)
        spells = [
            (53,  4, 0, 0, 0, 0),  # Magic Missile
            (73,  2, 2, 0, 0, 0),  # Drain
            (113, 0, 0, 6, 0, 0),  # Shield
            (173, 0, 0, 0, 6, 0),  # Poison
            (229, 0, 0, 0, 0, 5),  # Recharge
        ]

        for cost, dmg, heal, s_time, p_time, r_time in spells:
            if mana < cost:
                continue
            # Cannot cast an effect spell if that effect is still active
            if s_time > 0 and shield > 0:
                continue
            if p_time > 0 and poison > 0:
                continue
            if r_time > 0 and recharge > 0:
                continue

            # Cast spell
            next_mana_spent = mana_spent + cost
            next_mana = mana - cost
            next_hp = hp + heal
            next_boss_hp = boss_hp - dmg
            next_shield = s_time if s_time > 0 else shield
            next_poison = p_time if p_time > 0 else poison
            next_recharge = r_time if r_time > 0 else recharge

            if next_boss_hp <= 0:
                return next_mana_spent

            # --- 2. BOSS TURN ---
            # Apply active effects at the start of Boss turn
            armor = 0
            if next_shield > 0:
                armor = 7
                next_shield -= 1
            if next_poison > 0:
                next_boss_hp -= 3
                next_poison -= 1
            if next_recharge > 0:
                next_mana += 101
                next_recharge -= 1

            if next_boss_hp <= 0:
                return next_mana_spent

            # Boss attacks
            damage_dealt = max(1, boss_damage - armor)
            next_hp -= damage_dealt

            if next_hp > 0:
                heapq.heappush(
                    pq,
                    (
                        next_mana_spent,
                        next_hp,
                        next_mana,
                        next_boss_hp,
                        next_shield,
                        next_poison,
                        next_recharge,
                    ),
                )

    return -1  # No solution found

if __name__ == "__main__":
    # DATA
    data = {}
    with open("./data/data_22.txt") as file:
        for line in file:
            k,v = line.split(":")
            data[k.strip()] = int(v)

    hp = data["Hit Points"]
    dam = data["Damage"]

    print(f"Part 1: {min_mana_to_win(hp, dam, hard_mode=False)}")
    print(f"Part 2: {min_mana_to_win(hp, dam, hard_mode=True)}")