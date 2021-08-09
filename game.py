from web3 import Web3
import json
import time
from math import floor


bsc = "https://bsc-dataseed.binance.org/"
web3 = Web3(Web3.HTTPProvider(bsc))

oracle_address = '0x1CBFA0EC28dA66896946474B2A93856Eb725FbbA'
game_address = '0x39Bea96e13453Ed52A734B6ACEeD4c41F57B2271'
weapons_address = '0x7E091b0a220356B157131c831258A9C98aC8031A'
characters_address = '0xc6f252c2CdD4087e30608A35c022ce490B58179b'
skill_address = '0x154A9F9cbd3449AD22FDaE23044319D6eF2a1Fab'
defaultAddress = '0x0000000000000000000000000000000000000000'

abi_oracle = json.loads('[{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"currentPrice","type":"uint256"}],"name":"CurrentPriceUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"previousAdminRole","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"newAdminRole","type":"bytes32"}],"name":"RoleAdminChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleGranted","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleRevoked","type":"event"},{"inputs":[],"name":"DEFAULT_ADMIN_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"PRICE_UPDATER","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"currentPrice","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"}],"name":"getRoleAdmin","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"uint256","name":"index","type":"uint256"}],"name":"getRoleMember","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"}],"name":"getRoleMemberCount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"grantRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"hasRole","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"renounceRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"revokeRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_currentPrice","type":"uint256"}],"name":"setCurrentPrice","outputs":[],"stateMutability":"nonpayable","type":"function"}]')
abi_game = json.loads('[{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"uint256","name":"character","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"weapon","type":"uint256"},{"indexed":false,"internalType":"uint32","name":"target","type":"uint32"},{"indexed":false,"internalType":"uint24","name":"playerRoll","type":"uint24"},{"indexed":false,"internalType":"uint24","name":"enemyRoll","type":"uint24"},{"indexed":false,"internalType":"uint16","name":"xpGain","type":"uint16"},{"indexed":false,"internalType":"uint256","name":"skillGain","type":"uint256"}],"name":"FightOutcome","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"skillAmount","type":"uint256"}],"name":"InGameOnlyFundsGiven","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"previousAdminRole","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"newAdminRole","type":"bytes32"}],"name":"RoleAdminChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleGranted","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleRevoked","type":"event"},{"inputs":[],"name":"DEFAULT_ADMIN_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"GAME_ADMIN","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"REWARDS_CLAIM_TAX_DURATION","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"REWARDS_CLAIM_TAX_MAX","outputs":[{"internalType":"int128","name":"","type":"int128"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"characterID","type":"uint256"},{"internalType":"address","name":"playerAddress","type":"address"}],"name":"approveContractCharacterFor","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"weaponID","type":"uint256"},{"internalType":"address","name":"playerAddress","type":"address"}],"name":"approveContractWeaponFor","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"burnID","type":"uint256"}],"name":"burnWeapon","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"burnWeaponFee","outputs":[{"internalType":"int128","name":"","type":"int128"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256[]","name":"burnIDs","type":"uint256[]"}],"name":"burnWeapons","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"characters","outputs":[{"internalType":"contract Characters","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"claimTokenRewards","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"claimXpRewards","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"char","type":"uint256"},{"internalType":"uint256","name":"wep","type":"uint256"},{"internalType":"uint32","name":"target","type":"uint32"},{"internalType":"uint8","name":"fightMultiplier","type":"uint8"}],"name":"fight","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"fightRewardBaseline","outputs":[{"internalType":"int128","name":"","type":"int128"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"fightRewardGasOffset","outputs":[{"internalType":"int128","name":"","type":"int128"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"fightTraitBonus","outputs":[{"internalType":"int128","name":"","type":"int128"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"fightXpGain","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getCurrentHour","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint32","name":"target","type":"uint32"}],"name":"getMonsterPower","outputs":[{"internalType":"uint24","name":"","type":"uint24"}],"stateMutability":"pure","type":"function"},{"inputs":[],"name":"getMyCharacters","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getMyWeapons","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getOwnRewardsClaimTax","outputs":[{"internalType":"int128","name":"","type":"int128"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint24","name":"basePower","type":"uint24"},{"internalType":"int128","name":"weaponMultiplier","type":"int128"},{"internalType":"uint24","name":"bonusPower","type":"uint24"}],"name":"getPlayerPower","outputs":[{"internalType":"uint24","name":"","type":"uint24"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"uint24","name":"traitsCWE","type":"uint24"}],"name":"getPlayerTraitBonusAgainst","outputs":[{"internalType":"int128","name":"","type":"int128"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"}],"name":"getRoleAdmin","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"uint256","name":"index","type":"uint256"}],"name":"getRoleMember","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"}],"name":"getRoleMemberCount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"playerAddress","type":"address"},{"internalType":"uint256","name":"skillNeeded","type":"uint256"}],"name":"getSkillNeededFromUserWallet","outputs":[{"internalType":"uint256","name":"skillNeededFromUserWallet","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_inGameOnlyFunds","type":"uint256"},{"internalType":"uint256","name":"_tokenRewards","type":"uint256"},{"internalType":"uint256","name":"_skillNeeded","type":"uint256"}],"name":"getSkillToSubtract","outputs":[{"internalType":"uint256","name":"fromInGameOnlyFunds","type":"uint256"},{"internalType":"uint256","name":"fromTokenRewards","type":"uint256"},{"internalType":"uint256","name":"fromUserWallet","type":"uint256"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"uint256","name":"char","type":"uint256"},{"internalType":"uint256","name":"wep","type":"uint256"}],"name":"getTargets","outputs":[{"internalType":"uint32[4]","name":"","type":"uint32[4]"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getTokenRewards","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"wallet","type":"address"}],"name":"getTokenRewardsFor","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"wallet","type":"address"}],"name":"getTotalSkillOwnedBy","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"char","type":"uint256"}],"name":"getXpRewards","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"skillAmount","type":"uint256"}],"name":"giveInGameOnlyFunds","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"skillAmount","type":"uint256"}],"name":"giveInGameOnlyFundsFromContractBalance","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"grantRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"hasRole","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"inGameOnlyFunds","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"contract IERC20","name":"_skillToken","type":"address"},{"internalType":"contract Characters","name":"_characters","type":"address"},{"internalType":"contract Weapons","name":"_weapons","type":"address"},{"internalType":"contract IPriceOracle","name":"_priceOracleSkillPerUsd","type":"address"},{"internalType":"contract IRandoms","name":"_randoms","type":"address"}],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint8","name":"attacker","type":"uint8"},{"internalType":"uint8","name":"defender","type":"uint8"}],"name":"isTraitEffectiveAgainst","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"contract IRandoms","name":"_newRandoms","type":"address"}],"name":"migrateRandoms","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"contract IStakeFromGame","name":"_stakeFromGame","type":"address"}],"name":"migrateTo_23b3a8b","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"migrateTo_801f279","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"contract Promos","name":"_promos","type":"address"}],"name":"migrateTo_ef994e2","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"mintCharacter","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"mintCharacterFee","outputs":[{"internalType":"int128","name":"","type":"int128"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"mintWeapon","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"mintWeaponFee","outputs":[{"internalType":"int128","name":"","type":"int128"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"oneFrac","outputs":[{"internalType":"int128","name":"","type":"int128"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"playerAddress","type":"address"},{"internalType":"int128","name":"usdAmount","type":"int128"}],"name":"payContract","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"playerAddress","type":"address"},{"internalType":"uint256","name":"convertedAmount","type":"uint256"}],"name":"payContractConverted","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"playerAddress","type":"address"},{"internalType":"int128","name":"baseAmount","type":"int128"}],"name":"payPlayer","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"playerAddress","type":"address"},{"internalType":"uint256","name":"convertedAmount","type":"uint256"}],"name":"payPlayerConverted","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"priceOracleSkillPerUsd","outputs":[{"internalType":"contract IPriceOracle","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"promos","outputs":[{"internalType":"contract Promos","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"randoms","outputs":[{"internalType":"contract IRandoms","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"recoverSkill","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"refillStaminaFee","outputs":[{"internalType":"int128","name":"","type":"int128"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"reforgeID","type":"uint256"},{"internalType":"uint256","name":"burnID","type":"uint256"}],"name":"reforgeWeapon","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"reforgeWeaponFee","outputs":[{"internalType":"int128","name":"","type":"int128"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"reforgeID","type":"uint256"},{"internalType":"uint8","name":"amountLB","type":"uint8"},{"internalType":"uint8","name":"amount4B","type":"uint8"},{"internalType":"uint8","name":"amount5B","type":"uint8"}],"name":"reforgeWeaponWithDust","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"reforgeWeaponWithDustFee","outputs":[{"internalType":"int128","name":"","type":"int128"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"renounceRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"revokeRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"cents","type":"uint256"}],"name":"setBurnWeaponValue","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"max","type":"uint256"}],"name":"setCharacterLimit","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"cents","type":"uint256"}],"name":"setCharacterMintValue","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint8","name":"points","type":"uint8"}],"name":"setDurabilityCostFight","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"tenthcents","type":"uint256"}],"name":"setFightRewardBaselineValue","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"cents","type":"uint256"}],"name":"setFightRewardGasOffsetValue","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"average","type":"uint256"}],"name":"setFightXpGain","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"cents","type":"uint256"}],"name":"setReforgeWeaponValue","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"cents","type":"uint256"}],"name":"setReforgeWeaponWithDustValue","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint8","name":"points","type":"uint8"}],"name":"setStaminaCostFight","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"cents","type":"uint256"}],"name":"setWeaponMintValue","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"skillToken","outputs":[{"internalType":"contract IERC20","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"stakeFromGameImpl","outputs":[{"internalType":"contract IStakeFromGame","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"stakeUnclaimedRewards","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"totalInGameOnlyFunds","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint96","name":"playerData","type":"uint96"}],"name":"unpackFightData","outputs":[{"internalType":"uint8","name":"charTrait","type":"uint8"},{"internalType":"uint24","name":"basePowerLevel","type":"uint24"},{"internalType":"uint64","name":"timestamp","type":"uint64"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"int128","name":"usdAmount","type":"int128"}],"name":"usdToSkill","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint24","name":"playerBasePower","type":"uint24"},{"internalType":"int128","name":"wepMultiplier","type":"int128"},{"internalType":"uint24","name":"wepBonusPower","type":"uint24"},{"internalType":"uint64","name":"staminaTimestamp","type":"uint64"},{"internalType":"uint256","name":"hour","type":"uint256"},{"internalType":"uint32","name":"target","type":"uint32"}],"name":"verifyFight","outputs":[],"stateMutability":"pure","type":"function"},{"inputs":[],"name":"weapons","outputs":[{"internalType":"contract Weapons","name":"","type":"address"}],"stateMutability":"view","type":"function"}]')
abi_weapons = json.loads('[{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"approved","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"operator","type":"address"},{"indexed":false,"internalType":"bool","name":"approved","type":"bool"}],"name":"ApprovalForAll","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"uint256","name":"burned","type":"uint256"}],"name":"Burned","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"weapon","type":"uint256"},{"indexed":true,"internalType":"address","name":"minter","type":"address"}],"name":"NewWeapon","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"uint256","name":"reforged","type":"uint256"},{"indexed":true,"internalType":"uint256","name":"burned","type":"uint256"},{"indexed":false,"internalType":"uint8","name":"lowPoints","type":"uint8"},{"indexed":false,"internalType":"uint8","name":"fourPoints","type":"uint8"},{"indexed":false,"internalType":"uint8","name":"fivePoints","type":"uint8"}],"name":"Reforged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"uint256","name":"reforged","type":"uint256"},{"indexed":false,"internalType":"uint8","name":"lowDust","type":"uint8"},{"indexed":false,"internalType":"uint8","name":"fourDust","type":"uint8"},{"indexed":false,"internalType":"uint8","name":"fiveDust","type":"uint8"},{"indexed":false,"internalType":"uint8","name":"lowPoints","type":"uint8"},{"indexed":false,"internalType":"uint8","name":"fourPoints","type":"uint8"},{"indexed":false,"internalType":"uint8","name":"fivePoints","type":"uint8"}],"name":"ReforgedWithDust","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"previousAdminRole","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"newAdminRole","type":"bytes32"}],"name":"RoleAdminChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleGranted","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleRevoked","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[],"name":"DEFAULT_ADMIN_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"GAME_ADMIN","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"RECEIVE_DOES_NOT_SET_TRANSFER_TIMESTAMP","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"burnID","type":"uint256"}],"name":"_calculateBurnValues","outputs":[{"internalType":"uint8[]","name":"","type":"uint8[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"approve","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"baseURI","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"burnID","type":"uint256"}],"name":"burn","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"burnPointMultiplier","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"uint8","name":"amount","type":"uint8"}],"name":"drainDurability","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"fiveStarBurnPowerPerPoint","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"fourStarBurnPowerPerPoint","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"get","outputs":[{"internalType":"uint16","name":"_properties","type":"uint16"},{"internalType":"uint16","name":"_stat1","type":"uint16"},{"internalType":"uint16","name":"_stat2","type":"uint16"},{"internalType":"uint16","name":"_stat3","type":"uint16"},{"internalType":"uint8","name":"_level","type":"uint8"},{"internalType":"uint8","name":"_blade","type":"uint8"},{"internalType":"uint8","name":"_crossguard","type":"uint8"},{"internalType":"uint8","name":"_grip","type":"uint8"},{"internalType":"uint8","name":"_pommel","type":"uint8"},{"internalType":"uint24","name":"_burnPoints","type":"uint24"},{"internalType":"uint24","name":"_bonusPower","type":"uint24"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"getApproved","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"getBonusPower","outputs":[{"internalType":"uint24","name":"","type":"uint24"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"uint8","name":"level","type":"uint8"}],"name":"getBonusPowerForFight","outputs":[{"internalType":"uint24","name":"","type":"uint24"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getDurabilityMaxWait","outputs":[{"internalType":"uint64","name":"","type":"uint64"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"getDurabilityPoints","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint64","name":"timestamp","type":"uint64"}],"name":"getDurabilityPointsFromTimestamp","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"getDurabilityTimestamp","outputs":[{"internalType":"uint64","name":"","type":"uint64"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"playerAddress","type":"address"}],"name":"getDustSupplies","outputs":[{"internalType":"uint32[]","name":"","type":"uint32[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"uint8","name":"charTrait","type":"uint8"}],"name":"getFightData","outputs":[{"internalType":"int128","name":"","type":"int128"},{"internalType":"int128","name":"","type":"int128"},{"internalType":"uint24","name":"","type":"uint24"},{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"getLevel","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"getPowerMultiplier","outputs":[{"internalType":"int128","name":"","type":"int128"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"properties","type":"uint16"},{"internalType":"uint16","name":"stat1","type":"uint16"},{"internalType":"uint16","name":"stat2","type":"uint16"},{"internalType":"uint16","name":"stat3","type":"uint16"},{"internalType":"uint8","name":"trait","type":"uint8"}],"name":"getPowerMultiplierForTrait","outputs":[{"internalType":"int128","name":"","type":"int128"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"getProperties","outputs":[{"internalType":"uint16","name":"","type":"uint16"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"seed","type":"uint256"},{"internalType":"uint256","name":"seed2","type":"uint256"},{"internalType":"uint8","name":"limit","type":"uint8"}],"name":"getRandomCosmetic","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"uint256","name":"stars","type":"uint256"},{"internalType":"uint256","name":"seed","type":"uint256"}],"name":"getRandomProperties","outputs":[{"internalType":"uint16","name":"","type":"uint16"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"uint16","name":"minRoll","type":"uint16"},{"internalType":"uint16","name":"maxRoll","type":"uint16"},{"internalType":"uint256","name":"seed","type":"uint256"},{"internalType":"uint256","name":"seed2","type":"uint256"}],"name":"getRandomStat","outputs":[{"internalType":"uint16","name":"","type":"uint16"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"}],"name":"getRoleAdmin","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"uint256","name":"index","type":"uint256"}],"name":"getRoleMember","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"}],"name":"getRoleMemberCount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"getStars","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"properties","type":"uint16"}],"name":"getStarsFromProperties","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"getStat1","outputs":[{"internalType":"uint16","name":"","type":"uint16"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint8","name":"statPattern","type":"uint8"}],"name":"getStat1Trait","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"getStat2","outputs":[{"internalType":"uint16","name":"","type":"uint16"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint8","name":"statPattern","type":"uint8"}],"name":"getStat2Trait","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"getStat3","outputs":[{"internalType":"uint16","name":"","type":"uint16"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint8","name":"statPattern","type":"uint8"}],"name":"getStat3Trait","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"uint256","name":"stars","type":"uint256"}],"name":"getStatCount","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"uint256","name":"stars","type":"uint256"}],"name":"getStatMaxRoll","outputs":[{"internalType":"uint16","name":"","type":"uint16"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"uint256","name":"stars","type":"uint256"}],"name":"getStatMinRoll","outputs":[{"internalType":"uint16","name":"","type":"uint16"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"getStatPattern","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"properties","type":"uint16"}],"name":"getStatPatternFromProperties","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"getTrait","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"properties","type":"uint16"}],"name":"getTraitFromProperties","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"grantRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"hasRole","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"operator","type":"address"}],"name":"isApprovedForAll","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"isDurabilityFull","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"lastTransferTimestamp","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"lowStarBurnPowerPerPoint","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"maxDurability","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"migrateTo_951a020","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"migrateTo_aa9da90","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"migrateTo_e55d8c5","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"minter","type":"address"},{"internalType":"uint256","name":"seed","type":"uint256"}],"name":"mint","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"minter","type":"address"},{"internalType":"uint256","name":"stars","type":"uint256"},{"internalType":"uint256","name":"seed","type":"uint256"}],"name":"mintWeaponWithStars","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"oneFrac","outputs":[{"internalType":"int128","name":"","type":"int128"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"ownerOf","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"minter","type":"address"},{"internalType":"uint16","name":"properties","type":"uint16"},{"internalType":"uint16","name":"stat1","type":"uint16"},{"internalType":"uint16","name":"stat2","type":"uint16"},{"internalType":"uint16","name":"stat3","type":"uint16"},{"internalType":"uint256","name":"cosmeticSeed","type":"uint256"}],"name":"performMintWeapon","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"powerMultPerPointBasic","outputs":[{"internalType":"int128","name":"","type":"int128"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"powerMultPerPointMatching","outputs":[{"internalType":"int128","name":"","type":"int128"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"powerMultPerPointPWR","outputs":[{"internalType":"int128","name":"","type":"int128"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"reforgeID","type":"uint256"},{"internalType":"uint256","name":"burnID","type":"uint256"}],"name":"reforge","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"reforgeID","type":"uint256"},{"internalType":"uint8","name":"amountLB","type":"uint8"},{"internalType":"uint8","name":"amount4B","type":"uint8"},{"internalType":"uint8","name":"amount5B","type":"uint8"}],"name":"reforgeWithDust","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"renounceRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"revokeRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"bytes","name":"_data","type":"bytes"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"secondsPerDurability","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"operator","type":"address"},{"internalType":"bool","name":"approved","type":"bool"}],"name":"setApprovalForAll","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"multiplier","type":"uint256"}],"name":"setBurnPointMultiplier","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"uint64","name":"timestamp","type":"uint64"}],"name":"setDurabilityTimestamp","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"powerPerBurnPoint","type":"uint256"}],"name":"setFiveStarBurnPowerPerPoint","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"powerPerBurnPoint","type":"uint256"}],"name":"setFourStarBurnPowerPerPoint","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"powerPerBurnPoint","type":"uint256"}],"name":"setLowStarBurnPowerPerPoint","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"index","type":"uint256"}],"name":"tokenByIndex","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"uint256","name":"index","type":"uint256"}],"name":"tokenOfOwnerByIndex","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"tokenURI","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"transferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"}]')
abi_characters = json.loads('[{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"approved","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"operator","type":"address"},{"indexed":false,"internalType":"bool","name":"approved","type":"bool"}],"name":"ApprovalForAll","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"uint256","name":"character","type":"uint256"},{"indexed":false,"internalType":"uint16","name":"level","type":"uint16"}],"name":"LevelUp","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"character","type":"uint256"},{"indexed":true,"internalType":"address","name":"minter","type":"address"}],"name":"NewCharacter","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"previousAdminRole","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"newAdminRole","type":"bytes32"}],"name":"RoleAdminChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleGranted","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleRevoked","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[],"name":"DEFAULT_ADMIN_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"GAME_ADMIN","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"NO_OWNED_LIMIT","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"RECEIVE_DOES_NOT_SET_TRANSFER_TIMESTAMP","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"TRANSFER_COOLDOWN","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"approve","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"baseURI","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"characterLimit","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"uint16","name":"xp","type":"uint16"}],"name":"gainXp","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"get","outputs":[{"internalType":"uint16","name":"","type":"uint16"},{"internalType":"uint8","name":"","type":"uint8"},{"internalType":"uint8","name":"","type":"uint8"},{"internalType":"uint64","name":"","type":"uint64"},{"internalType":"uint16","name":"","type":"uint16"},{"internalType":"uint16","name":"","type":"uint16"},{"internalType":"uint16","name":"","type":"uint16"},{"internalType":"uint16","name":"","type":"uint16"},{"internalType":"uint16","name":"","type":"uint16"},{"internalType":"uint16","name":"","type":"uint16"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"getApproved","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"uint8","name":"amount","type":"uint8"}],"name":"getFightDataAndDrainStamina","outputs":[{"internalType":"uint96","name":"","type":"uint96"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"getLevel","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"getPower","outputs":[{"internalType":"uint24","name":"","type":"uint24"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint8","name":"level","type":"uint8"}],"name":"getPowerAtLevel","outputs":[{"internalType":"uint24","name":"","type":"uint24"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"uint8","name":"currentLevel","type":"uint8"}],"name":"getRequiredXpForNextLevel","outputs":[{"internalType":"uint16","name":"","type":"uint16"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"}],"name":"getRoleAdmin","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"uint256","name":"index","type":"uint256"}],"name":"getRoleMember","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"}],"name":"getRoleMemberCount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getStaminaMaxWait","outputs":[{"internalType":"uint64","name":"","type":"uint64"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"getStaminaPoints","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint64","name":"timestamp","type":"uint64"}],"name":"getStaminaPointsFromTimestamp","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"getStaminaTimestamp","outputs":[{"internalType":"uint64","name":"","type":"uint64"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"getTrait","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"getXp","outputs":[{"internalType":"uint32","name":"","type":"uint32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"grantRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"hasRole","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"operator","type":"address"}],"name":"isApprovedForAll","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"isStaminaFull","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"lastTransferTimestamp","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"maxStamina","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"migrateTo_1ee400a","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"migrateTo_951a020","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"migrateTo_b627f23","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"contract Promos","name":"_promos","type":"address"}],"name":"migrateTo_ef994e2","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"minter","type":"address"},{"internalType":"uint256","name":"seed","type":"uint256"}],"name":"mint","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"ownerOf","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"promos","outputs":[{"internalType":"contract Promos","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"renounceRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"revokeRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"bytes","name":"_data","type":"bytes"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"secondsPerStamina","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"operator","type":"address"},{"internalType":"bool","name":"approved","type":"bool"}],"name":"setApprovalForAll","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"max","type":"uint256"}],"name":"setCharacterLimit","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"uint64","name":"timestamp","type":"uint64"}],"name":"setStaminaTimestamp","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"index","type":"uint256"}],"name":"tokenByIndex","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"uint256","name":"index","type":"uint256"}],"name":"tokenOfOwnerByIndex","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"tokenURI","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"transferCooldownEnd","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"transferCooldownLeft","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"transferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"}]')
abi_skill = json.loads('[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"unpause","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"account","type":"address"},{"name":"amount","type":"uint256"}],"name":"mint","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_value","type":"uint256"}],"name":"burn","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"paused","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_subtractedValue","type":"uint256"}],"name":"decreaseApproval","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"listAddress","type":"address"},{"name":"isBlackListed","type":"bool"}],"name":"blackListAddress","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"pause","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_addedValue","type":"uint256"}],"name":"increaseApproval","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"inputs":[{"name":"_name","type":"string"},{"name":"_symbol","type":"string"},{"name":"_decimals","type":"uint256"},{"name":"_supply","type":"uint256"},{"name":"tokenOwner","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Mint","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"burner","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Burn","type":"event"},{"anonymous":false,"inputs":[],"name":"Pause","type":"event"},{"anonymous":false,"inputs":[],"name":"Unpause","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"previousOwner","type":"address"},{"indexed":true,"name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"blackListed","type":"address"},{"indexed":false,"name":"value","type":"bool"}],"name":"Blacklist","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"}]')

oracle_contract = web3.eth.contract(address=oracle_address, abi=abi_oracle)
game_contract = web3.eth.contract(address=game_address, abi=abi_game)
weapons_contract = web3.eth.contract(address=weapons_address, abi=abi_weapons)
characters_contract = web3.eth.contract(address=characters_address, abi=abi_characters)
skill_contract = web3.eth.contract(address=skill_address, abi=abi_skill)

WeaponElement = {
    'Fire': 0,
    'Earth': 1,
    'Lightning': 2,
    'Water': 3
}
WeaponTrait = {
    'STR': 0,
    'DEX': 1,
    'CHA': 2,
    'INT': 3,
    'PWR': 4
}

def trait_number_to_name(trait_num):
    return WeaponElement

def character_power(level):
    return (1000 + (level * 10)) * (floor(level / 10) + 1)

def get_targets_enemy(chars, weapon):
    return game_contract.functions.getTargets(chars, weapon).call()

def character(address):
    return game_contract.functions.getMyCharacters().call({'from': address})

def characters_info(character_id):
    get_char_info = characters_contract.functions.get(character_id).call()
    xp = get_char_info[0]
    level_char = int(get_char_info[1])
    trait = get_char_info[2]
    # train_name = get_trait_name(get_char_info[2])
    stamina_timestamp = get_char_info[3]
    head = get_char_info[4]
    arms = get_char_info[5]
    torso = get_char_info[6]
    legs = get_char_info[7]
    boots = get_char_info[8]
    race = get_char_info[9]

    return {
        'id': character_id,
        'xp': xp,
        'level': level_char,
        'trait': trait,
        'stamina': stamina_timestamp,
        'head': head,
        'arms': arms,
        'torso': torso,
        'legs': legs,
        'boots': boots,
        'race': race
    }

def weapons(address):
    return game_contract.functions.getMyWeapons().call({'from': address})

def weapon_info(weapon_id):
    def get_stat_pattern_from_properties(properties):
        return weapons_contract.functions.getStatPatternFromProperties(properties).call()

    def get_stat1_trait(stat_pattern):
        return stat_pattern % 5

    def get_stat2_trait(stat_pattern):
        return floor(stat_pattern / 5) % 5

    def get_stat3_trait(stat_pattern):
        return floor(floor(stat_pattern / 5) / 5) % 5

    def get_weapons_trait_from_properties(properties):
        return weapons_contract.functions.getTraitFromProperties(properties).call()

    get_weapon_info = weapons_contract.functions.get(weapon_id).call()
    properties = get_weapon_info[0]
    stat1 = get_weapon_info[1]
    stat2 = get_weapon_info[2]
    stat3 = get_weapon_info[3]
    level_weapon = get_weapon_info[4]
    blade = get_weapon_info[5]
    crossguard = get_weapon_info[6]
    grip = get_weapon_info[7]
    pommel = get_weapon_info[8]
    burn_points = get_weapon_info[9]
    bonus_power = get_weapon_info[10]

    stat_pattern = get_stat_pattern_from_properties(properties)
    stat1_type = get_stat1_trait(stat_pattern)
    stat2_type = get_stat2_trait(stat_pattern)
    stat3_type = get_stat3_trait(stat_pattern)

    trait_num = get_weapons_trait_from_properties(properties)

    low_star_burn_points = burn_points & 0xff
    four_star_burn_points = (burn_points >> 8) & 0xff
    five_star_burn_points = (burn_points >> 16) & 0xff

    stars = properties & 0x7

    return {
        'id': weapon_id,
        'properties': properties,
        'train_num': trait_num,
        'stat1': stat1,
        'stat1_type': stat1_type,
        'stat2': stat2,
        'stat2_type': stat2_type,
        'stat3': stat3,
        'stat3_type': stat3_type,
        'level_weapon': level_weapon,
        'blade': blade,
        'crossguard': crossguard,
        'grip': grip,
        'pommel': pommel,
        'stars': stars,
        'low_star_burn_points': low_star_burn_points,
        'four_star_burn_points': four_star_burn_points,
        'five_star_burn_points': five_star_burn_points,
        'bonus_power': bonus_power
    }

def get_enemy_details(targets):
    return {
        'targetEnemy': targets,
        'enemyPower': game_contract.functions.getMonsterPower(targets).call(),
        'traitEnemy': targets >> 24
    }

def get_winner_chance(chars_data, weapon):
    def get_total_multiplier_for_traits(weap_data, pl_elem):
        def multi(stat_value):
            return stat_value * 0.25

        def adj(statv, sttrait, chtrait):
            if sttrait == chtrait:
                statv = floor(statv * 1.07)
            elif sttrait == 4:
                statv = floor(statv * 1.03)
            return statv

        def stat1(weap, trait):
            return multi(adj(weap['stat1'], weap['stat1_type'], trait))

        def stat2(weap, trait):
            return multi(adj(weap['stat2'], weap['stat2_type'], trait))

        def stat3(weap, trait):
            return multi(adj(weap['stat3'], weap['stat3_type'], trait))

        return 1 + (0.01 * (stat1(weap_data, pl_elem) + stat2(weap_data, pl_elem)
                            + stat3(weap_data, pl_elem)))

    def get_element_advantage(player_elem, enemy_elem):
        if (player_elem + 1) % 4 == enemy_elem:
            return 1
        if (enemy_elem + 1) % 4 == player_elem:
            return -1
        return 0

    weapon_data = weapon_info(weapon)
    for chars in chars_data:
        mx = []
        targets = get_targets_enemy(chars, weapon_data['id'])
        tgs = list(map(get_enemy_details, targets))
        for ind in range(len(tgs)):
            enemy_element = tgs[ind]['traitEnemy']
            char_data = characters_info(chars)
            char_power = character_power(char_data['level'])
            player_element = char_data['trait']
            weapon_element = weapon_data['train_num']
            enemy_power = tgs[ind]['enemyPower']
            target_enemy = tgs[ind]['targetEnemy']
            # weapon_multiplier = get_total_multiplier_for_trait(weapon_data, player_element)
            weapon_multiplier1 = get_total_multiplier_for_traits(weapon_data, player_element)
            total_power = (char_power * weapon_multiplier1) + weapon_data['bonus_power']
            total_multiplier = 1 + (0.075 * (1 if weapon_element == player_element else 0) +
                                    (0.075 * get_element_advantage(player_element, enemy_element)))
            player_min = total_power * total_multiplier * 0.9
            player_max = total_power * total_multiplier * 1.1
            player_range = player_max - player_min
            enemy_min = enemy_power * 0.9
            enemy_max = enemy_power * 1.1
            enemy_range = enemy_max - enemy_min
            rolling_total = 0

            if player_max < enemy_min:
                return 0
            if player_min >= enemy_min:
                rolling_total = (player_min - enemy_min) / enemy_range
                rolling_total += (1 - rolling_total) * ((player_max - enemy_max) / player_range)
                rolling_total += (1 - rolling_total) * 0.5
            else:
                rolling_total = (enemy_min - player_min) / player_range
                rolling_total += (1 - rolling_total) * ((enemy_max - player_max) / enemy_range)
                rolling_total += (1 - rolling_total) * 0.5
                rolling_total = 1 - rolling_total
            mx.append({
                'charId': char_data['id'],
                'weaponId': weapon_data['id'],
                'targetEnemy': target_enemy,
                'winChance': float("{0:.4}".format(rolling_total * 100))
            })
        yield mx[max(range(len(mx)), key=lambda index: mx[index]['winChance'])]

def get_xp(id_char):
    for xp_char in id_char:
        get_xp_character = game_contract.functions.getXpRewards(xp_char).call()
        yield get_xp_character

def get_stamina(id_char):
    return characters_contract.functions.getStaminaPoints(id_char).call()

def call_char(id_char):
    charer = characters_info(id_char)
    level = charer['level'] + 1
    trait = charer['trait']
    stamina = get_stamina(id_char)
    return {
        'id': id_char,
        'level': level,
        'trait': trait,
        'stamina': stamina
    }

def call_weapon(id_weapon):
    wwp = weapon_info(id_weapon)
    main_trait = wwp['train_num']
    stars = wwp['stars'] + 1
    bonus_power = wwp['bonus_power']
    if stars == 3:
        return {
            'id': id_weapon,
            'mainTrait': main_trait,
            'stars': stars,
            'bonusPower': bonus_power
        }

def fights(char_id, weapon_id, target_enemy, stamina_multiplier, winner_chance, main_address, private_key):
    try:
        nonce = web3.eth.get_transaction_count(main_address)
        '''blok = web3.eth.block_number
        if blok == blocks[-1]:
            time.sleep(2)
        try:
            nonce = nonces[-1] + 1 if nonce in nonces else nonce
        except Exception:
            pass'''
        fight = game_contract.functions.fight(char_id, weapon_id, target_enemy, stamina_multiplier).buildTransaction({
            'chainId': 56, 'gas': 240000, 'gasPrice': web3.toWei('5', 'gwei'), 'nonce': nonce
        })
        sign_fight = web3.eth.account.sign_transaction(fight, private_key=private_key)
        tx_hash = web3.eth.send_raw_transaction(sign_fight.rawTransaction)
        # nonces.append(nonce)
        # blocks.append(blok)
        # time.sleep(5)
        receipts = web3.eth.wait_for_transaction_receipt(web3.toHex(tx_hash), 240)
        logs = game_contract.events.FightOutcome().processReceipt(receipts)
        if logs[0]['args']['playerRoll'] > logs[0]['args']['enemyRoll']:
            return f'Победил с {winner_chance}%. {stamina_multiplier * 40}'
        else:
            return f'Проиграл с {winner_chance}%. {stamina_multiplier * 40}'
        time.sleep(5)
    except ValueError:
        return 'Произошла ошибка'

def call_figth(char_id, weapon_id, target_enemy, winner_chance, main_address, private_key):
    char_stamina = get_stamina(char_id)
    stamina_multiplier = 0
    if char_stamina < 80:
        return 'Нет стамины'
    else:
        if winner_chance >= 92:
            stamina_multiplier = char_stamina // 40
        else:
            stamina_multiplier = 1
        return fights(char_id, weapon_id, target_enemy, stamina_multiplier, winner_chance, main_address, private_key)

def get_xp_rewards(char_id):
    return game_contract.functions.getXpRewards(char_id).call()

def claim_xp_chars(address, pkey):
    if get_xp_rewards(character(address)[0]) != 0:
        nonce = web3.eth.get_transaction_count(address)
        xp = game_contract.functions.claimXpRewards().buildTransaction({
            'chainId': 56, 'gas': 900000, 'gasPrice': web3.toWei('5', 'gwei'), 'nonce': nonce
        })
        sign_xp = web3.eth.account.sign_transaction(xp, private_key=pkey)
        tx_hash = web3.eth.send_raw_transaction(sign_xp.rawTransaction)
        web3.eth.wait_for_transaction_receipt(web3.toHex(tx_hash), 240)
        return 'Забрал xp'
    else:
        return 'Нету xp'

def get_token_rewards(address):
    return game_contract.functions.getTokenRewards().call({'from': address})

def claim_rewards(address, pkey):
    if get_token_rewards(address) != 0:
        nonce = web3.eth.get_transaction_count(address)
        rewards = game_contract.functions.claimTokenRewards().buildTransaction({
            'chainId': 56, 'gas': 240000, 'gasPrice': web3.toWei('5', 'gwei'), 'nonce': nonce
        })
        sign_rewards = web3.eth.account.sign_transaction(rewards, private_key=pkey)
        tx_hash = web3.eth.send_raw_transaction(sign_rewards.rawTransaction)
        data = web3.eth.wait_for_transaction_receipt(web3.toHex(tx_hash), 240)
        logs = skill_contract.events.Transfer().processReceipt(data)
        return f"Ты зачем отобрал у игры {web3.fromWei(logs[0]['args']['value'], 'ether')} SKILL?"
    else:
        return 'Карманы пусты, милорд..'

def check_skill_balance(address):
    return skill_contract.functions.balanceOf(address).call()

def transfer(address, pkey, balance, main):
    if balance >= 0.05:
        nonce = web3.eth.get_transaction_count(address)
        transfer_build = skill_contract.functions.transfer(main, balance).buildTransaction({
            'chainId': 56, 'gas': 240000, 'gasPrice': web3.toWei('5', 'gwei'), 'nonce': nonce
        })
        sign_transfer = web3.eth.account.sign_transaction(transfer_build, private_key=pkey)
        tx_hash = web3.eth.send_raw_transaction(sign_transfer.rawTransaction)
        data = web3.eth.wait_for_transaction_receipt(web3.toHex(tx_hash), 240)
        logs = skill_contract.events.Transfer().processReceipt(data)
        return f"С адреса {address} было переведено {web3.fromWei(logs[0]['args']['value'], 'ether')} SKILL"
    else:
        return f'Дурачок, у тебя {balance} SKILL, что ты собрался переводить?'

def check_bnb_balance(address):
    return web3.fromWei(web3.eth.get_balance(address), 'ether')

if __name__ == '__main__':
    while True:
        caller = int(input('Выберите команду: '))
        if caller == 1:
            for confg in config.conf:
                main_address = confg.split(';')[0]
                private_key = confg.split(';')[1]
                all_chars = character(main_address)
                for allc in all_chars:
                    char = call_char(allc)
                    print(f'id персонажа: {char["id"]} лвл: {char["level"]} стамина: {char["stamina"]} '
                          f'стихия: {char["trait"]}')
                # test = characters_info(int(input('Введите id персонажа: ')))
                all_weapons = weapons(main_address)
                for allw in all_weapons:
                    try:
                        weapon = call_weapon(allw)
                        print(f'id оружия: {weapon["id"]} основная характеристика: {weapon["mainTrait"]} '
                              f'звезды: {weapon["stars"]}бонус силы: {weapon["bonusPower"]}')
                    except Exception:
                        pass
                # print(weapon)
                # test1 = weapon_info(int(input('Введите id оружия: ')))
                nonces = []
                blocks = [web3.eth.block_number]
                for char in get_winner_chance(all_chars, weapon['id']): # weapon['id']
                    call_figth(char['charId'], char['weaponId'], char['targetEnemy'], char['winChance'])
        elif caller == 2:
            for confg in config.conf:
                main_address = confg.split(';')[0]
                private_key = confg.split(';')[1]
                skill_balance = check_skill_balance(main_address)
                transfer(main_address, private_key, skill_balance)
        elif caller == 3:
            print(web3.fromWei(check_skill_balance(input('Введите кошелек для проверки баланса: ')), 'ether'), 'SKILL')
        elif caller == 4:
            # claim_xp_chars(input('адрес: '), input('кей: '))
            for confg in config.conf:
                main_address = confg.split(';')[0]
                private_key = confg.split(';')[1]
                claim_xp_chars(main_address, private_key)
        else:
            for confg in config.conf:
                main_address = confg.split(';')[0]
                private_key = confg.split(';')[1]
                claim_rewards(main_address, private_key)
