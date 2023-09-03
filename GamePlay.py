import math
import random


class Game:
    def __init__(self, player0, player1, battle):
        self.player0 = player0
        self.player1 = player1

        self.battle = battle

        self.attacker = None
        self.opponent = None

        self.attack_move = None
        self.opponent_move = None

        self.shield = False

    def damage(self):
        if self.attacker.moves[self.attack_move]['type'] == 'Neutral':
            p = 0
        else:
            p = self.attacker.moves[self.attack_move]['power']
        d = self.opponent.defense

        damage = math.floor(math.floor(p * p / d) / 20) + 2
        if self.shield:
            damage = 0
        self.opponent.health -= damage
        self.shield = False
        if self.game_over():
            return True

    def check_speed(self):
        if self.player0.speed == self.player1.speed:
            return random.choice([0, 1])
        elif self.player0.speed < self.player1.speed:
            return 1
        else:
            return 0

    def check_turn(self, move0, move1):
        if self.player0.moves[move0]['priority'] == self.player1.moves[move1]['priority']:
            self.attacker, self.opponent = self.player0, self.player1

            self.attack_move, self.opponent_move = move0, move1

            if self.check_speed() == 1:
                self.attacker, self.opponent = self.player1, self.player0

                self.attack_move, self.opponent_move = move1, move0

        else:
            s = sum([self.player0.moves[move0]['priority'], self.player1.moves[move1]['priority']])
            rand = random.uniform(0, s)
            if rand < self.player0.moves[move0]['priority']:
                self.attacker = self.player0
                self.opponent = self.player1

                self.attack_move, self.opponent_move = move0, move1
            else:
                self.attacker = self.player1
                self.opponent = self.player0

                self.attack_move, self.opponent_move = move1, move0

    def pending(self):
        self.attacker, self.opponent = self.opponent, self.attacker
        self.attack_move, self.opponent_move = self.opponent_move, self.attack_move

    def game_over(self):
        if self.player0.health <= 0:
            print(f"{self.player0.name} FAINTED")
            title = f"{self.player0.name} FAINTED"
            self.battle.battle_end(title)
            return True
        elif self.player1.health <= 0:
            print(f"{self.player1.name} FAINTED")
            title = f"{self.player1.name} FAINTED"
            self.battle.battle_end(title)
            return True

        return False

    def choose_move(self):
        print(f"{self.player0.name} HEALTH {self.player0.health}")
        i = 0
        for m in self.player0.moves:
            print(f"{i}) {m}")
            i += 1
        move0 = int(input('select a move: '))
        self.player0.moves[move0]['size'] -= 1

        print(f"{self.player1.name} HEALTH {self.player1.health}")
        i = 0
        for m in self.player1.moves:
            print(f"{i}) {m}")
            i += 1
        move1 = int(input('select a move: '))
        self.player1.moves[move1]['size'] -= 1

        return move0, move1

    def use_shield(self, choice):  # a player will always have a defense move!
        move = None
        for m in self.opponent.moves:
            if m['type'] == 'Defense':
                if m['size'] > 0:
                    move = m
                else:
                    self.shield = False
                    return False
                break
        if move:
            #choice = str(input(f"{self.opponent.name} defend ? [y/n] "))
            if choice == 'y':
                self.shield = True
                #print(f"{self.opponent.name} used {move['name']} and avoided the attack")
                move['size'] -= 1
                if move['size'] == 0:
                    self.opponent.moves.remove(move)
                return f"{self.opponent.name} used {move['name']} and avoided the attack"
            else:
                self.shield = False
                return False
        else:
            self.shield = False

    def check_moves(self, move0, move1):
        #self.player0.moves[move0]['size'] -= 1
        #self.player1.moves[move1]['size'] -= 1
        if self.player0.moves[move0]['size'] == 0:
            self.player0.moves.remove(self.player0.moves[move0])
        if self.player1.moves[move1]['size'] == 0:
            self.player1.moves.remove(self.player1.moves[move1])

    def fight(self):
        #(move0, move1) = self.choose_move()
        #self.check_turn(move0, move1)
        print(f"{self.attacker.name} used {self.attacker.moves[self.attack_move]['name']}")
        #self.use_shield('response')
        #self.damage()
        #self.pending()
        print(f"{self.attacker.name} used {self.attacker.moves[self.attack_move]['name']}")
        #self.use_shield()
        #self.damage()
        #self.check_moves(move0, move1)
        #self.fight()


