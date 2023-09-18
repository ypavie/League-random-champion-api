<template>
  <div class="grid grid-cols-12" style="display: flex;">
    <div class="col-span-3 sm:col-span-3">
      <div class="champion-portrait">
        <img src="https://raw.githubusercontent.com/InFinity54/LoL_DDragon/master/latest/img/champion/Aatrox.png"
          alt="Bel'Veth" class="img-responsive">
      </div>
    </div>
    <div class="col-span-9 sm:col-span-9">
      <p class="champion-name" style="font-size: 30px;">Le père Aatrox</p>
    </div>
    <div class="col-span-9 sm:col-span-9">
      <div>
        <div class="items" style="display: flex;">
          <div title="Mobility Boots" class="item">
            <img src="https://ddragon.leagueoflegends.com/cdn/13.15.1/img/item/3117.png" alt="Mobility Boots">
          </div>
          <div title="Rod of Ages" class="item">
            <img src="https://ddragon.leagueoflegends.com/cdn/13.15.1/img/item/6657.png" alt="Rod of Ages">
          </div>
          <div title="Nashor's Tooth" class="item">
            <img src="https://ddragon.leagueoflegends.com/cdn/13.15.1/img/item/3115.png" alt="Nashor's Tooth">
          </div>
          <div title="Prowler's Claw" class="item">
            <img src="https://ddragon.leagueoflegends.com/cdn/13.15.1/img/item/6693.png" alt="Prowler's Claw">
          </div>
          <div title="Staff of Flowing Water" class="item">
            <img src="https://ddragon.leagueoflegends.com/cdn/13.15.1/img/item/3003.png" alt="Staff of Flowing Water">
          </div>
          <div title="Phantom Dancer" class="item">
            <img src="https://ddragon.leagueoflegends.com/cdn/13.15.1/img/item/3046.png" alt="Phantom Dancer">
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="grid grid-cols-12 mt-3">
    <div class="col-span-3 sm:col-span-3">
      <div class="spells-mastery">
        <div class="spell-to-max">
          <img src="https://ddragon.leagueoflegends.com/cdn/13.16.1/img/spell/AatroxE.png" alt="Royal Maelstrom"
            title="Royal Maelstrom">
        </div>

        <div class="summoner-spells">
          <img src="https://ddragon.leagueoflegends.com/cdn/13.16.1/img/spell/SummonerHaste.png" alt="Cleanse"
            title="Cleanse">
          <img src="https://ddragon.leagueoflegends.com/cdn/13.16.1/img/spell/SummonerDot.png" alt="Ignite"
            title="Ignite">
        </div>
      </div>
      <div class="runes">
        <div class="runes-primary">
          <div class="runes-progress resolve">
            <div></div>
          </div>
          <ul>
            <li>
              <div class="main-rune-icon" title="Grasp of the Undying">
                <img
                  src="https://ddragon.leagueoflegends.com/cdn/img/perk-images/Styles/Resolve/GraspOfTheUndying/GraspOfTheUndying.png"
                  alt="Grasp of the Undying">
              </div>
            </li>
            <li>
              <div class="rune-icon" title="Grasp of the Undying">
                <img src="https://ddragon.leagueoflegends.com/cdn/img/perk-images/Styles/Resolve/Demolish/Demolish.png"
                  alt="Grasp of the Undying">
              </div>
            </li>
            <li>
              <div class="rune-icon" title="Grasp of the Undying">
                <img
                  src="https://ddragon.leagueoflegends.com/cdn/img/perk-images/Styles/Resolve/Conditioning/Conditioning.png"
                  alt="Grasp of the Undying">
              </div>
            </li>
            <li>
              <div class="rune-icon" title="Grasp of the Undying">
                <img
                  src="https://ddragon.leagueoflegends.com/cdn/img/perk-images/Styles/Sorcery/Unflinching/Unflinching.png"
                  alt="Grasp of the Undying">
              </div>
            </li>
          </ul>
        </div>
        <div class="runes-secondary">
          <div class="runes-progress resolve">
            <div></div>
          </div>
          <ul>
            <li>
              <div class="main-rune-icon">
                <img
                  src="https://ddragon.leagueoflegends.com/cdn/img/perk-images/Styles/Resolve/GraspOfTheUndying/GraspOfTheUndying.png"
                  alt="Grasp of the Undying" style="visibility: hidden;">
              </div>
            </li>
            <li>
              <div class="rune-icon">
                <img
                  src="https://ddragon.leagueoflegends.com/cdn/img/perk-images/Styles/Resolve/GraspOfTheUndying/GraspOfTheUndying.png"
                  alt="Grasp of the Undying" style="visibility: hidden;">
              </div>
            </li>
            <li>
              <div class="rune-icon" title="Grasp of the Undying">
                <img
                  src="https://ddragon.leagueoflegends.com/cdn/img/perk-images/Styles/Resolve/Conditioning/Conditioning.png"
                  alt="Grasp of the Undying">
              </div>
            </li>
            <li>
              <div class="rune-icon" title="Grasp of the Undying">
                <img
                  src="https://ddragon.leagueoflegends.com/cdn/img/perk-images/Styles/Sorcery/Unflinching/Unflinching.png"
                  alt="Grasp of the Undying">
              </div>
            </li>
          </ul>
        </div>
        <div class="rune-stats">
          <div class="rune-icon" title="Attack Speed (9% Attack Speed)">
            <img src="https://ddragon.leagueoflegends.com/cdn/img/perk-images/StatMods/StatModsAdaptiveForceIcon.png"
              height="30" alt="Attack Speed (9% Attack Speed)">
          </div>
          <div class="rune-icon" title="Magic Resist (6 MR)">
            <img src="https://ddragon.leagueoflegends.com/cdn/img/perk-images/StatMods/StatModsAdaptiveForceIcon.png"
              height="30" alt="Magic Resist (6 MR)">
          </div>
          <div class="rune-icon" title="Scaling Health (15-90 HP, lvls 1-18)">
            <img src="https://ddragon.leagueoflegends.com/cdn/img/perk-images/StatMods/StatModsHealthScalingIcon.png"
              height="30" alt="Scaling Health (15-90 HP, lvls 1-18)">
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    champion: Object,
  },
};
</script>

<style>
img {
  width: 50px;
  height: 50px;
}

.items,
.summoner-spells,
.spell-to-max {
  display: inline-flex;
  flex-direction: row;
  border: 1px solid #6f672a;
  border-radius: 3px;
  background-color: #0c5858;
  padding: 6px;
  margin: 0px 5px;
}

.runes-secondary li {
  list-style-type: none;
  padding: 0px;

}

/* CSS classes for your styles */

/* Add any global styles here */



.champion-portrait img {
  width: 75px;
  height: 75px;
}

.champion-name {
  font-size: 30px;
}

.items {
  display: flex;
}

.item {
  margin-right: 10px;
}

/* Define other CSS classes for your styles */

.spells-mastery {
  display: flex;
}

.spell-to-max {
  position: relative;
}

.summoner-spells img {
  /* Add any styles you need for summoner spells here */
}

.runes {
  display: flex;
  margin-top: 20px;
}

.runes-primary .runes-secondary {
  display: flex;
  flex-direction: column;
  position: relative;

  /*center child elements*/
  align-items: center;
}

.runes-progress {
  /* Add any styles for rune progress here */
}

ul {
  list-style-type: none;
  padding: 0;
}

.main-rune-icon img {
  width: 60px;
  height: 60px;
  margin-left: 20px;
  position: relative;
}

.rune-icon {
  width: 40px;
  height: 40px;
  margin-left: 30px;
  position: relative;
}

.rune-icon img {
  position: absolute;
  max-width: 100%;
  max-height: 100%;
}


.rune-stats {
  margin-top: 50px;
}

/* Add any additional styles you need */
</style>
