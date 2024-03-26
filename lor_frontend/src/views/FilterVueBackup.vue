<template>
  <div class="container">
    <div class="filter-group">
      <div class="champion-class">
        <label for="champion-class">Champion Class:</label>
        <div class="class-icons">
          <div class="class-icon" v-for="(icon, classType) in classes" :key="classType" @click="selectedTag = classType">
            <img :src="icon" :alt="classType">
            <span class="class-name">{{ classType }}</span>
          </div>
        </div>
      </div>

      <div class="region-group">
        <label for="region">Region:</label>
        <div class="region-icons">
          <div class="region-icon" v-for="(icon, region) in regions" :key="region" @click="selectedRegion = region">
            <img :src="icon" :alt="region">
            <span class="region-name">{{ region }}</span>
          </div>
        </div>
      </div>

      <div class="gender-group">
        <label for="gender">Gender:</label>
        <div class="gender">
            <input type="radio" id="gender-any" name="gender" value="Any" v-model="selectedGender">
            <label for="gender-any">Any</label>
            <input type="radio" id="gender-male" name="gender" value="Male" v-model="selectedGender">
            <label for="gender-male">Male</label>
            <input type="radio" id="gender-female" name="gender" value="Female" v-model="selectedGender">
            <label for="gender-female">Female</label>
            <input type="radio" id="gender-other" name="gender" value="Other" v-model="selectedGender">
            <label for="gender-other">Other</label>
        </div>
    </div>

    <div class="species-group">
        <label for="species">Specie:</label>
        <select id="species" v-model="selectedSpecies">
            <option value="Any">Any</option>
            <option v-for="specie in species" :key="specie" :value="specie">{{ specie }}</option>
        </select>
    </div>

    <div class="resource-group">
        <label for="partype">Resource:</label>
        <div class="partype">
            <input type="radio" id="resource-any" name="partype" value="Any" v-model="selectedPartype">
            <label for="resource-any">Any</label>
            <input type="radio" id="resource-mana" name="partype" value="Mana" v-model="selectedPartype">
            <label for="resource-mana">Mana</label>
            <input type="radio" id="resource-manaless" name="partype" value="Manaless" v-model="selectedPartype">
            <label for="resource-manaless">Manaless</label>
            <input type="radio" id="resource-other" name="partype" value="Other" v-model="selectedPartype">
            <label for="resource-other">Other</label>
        </div>
    </div>

    <div class="range-group">
        <label for="range-type">Range Type:</label>
        <div class="range-type">
            <input type="radio" id="range-any" name="range-type" value="Any" v-model="selectedRangeType">
            <label for="range-any">Any</label>
            <input type="radio" id="range-melee" name="range-type" value="Melee" v-model="selectedRangeType">
            <label for="range-melee">Melee</label>
            <input type="radio" id="range-ranged" name="range-type" value="Ranged" v-model="selectedRangeType">
            <label for="range-ranged">Ranged</label>
            <input type="radio" id="range-both" name="range-type" value="Both" v-model="selectedRangeType">
            <label for="range-both">Both</label>
        </div>
    </div>

    <div class="invoke-group">
        <label for="invoke-type">Can invoke:</label>
        <div class="invoke-type">
            <input type="radio" id="invoke-any" name="invoke-type" value="Any" v-model="selectedInvokeType">
            <label for="invoke-any">Any</label>
            <input type="radio" id="invoke-yes" name="invoke-type" value="Yes" v-model="selectedInvokeType">
            <label for="invoke-yes">Yes</label>
            <input type="radio" id="invoke-no" name="invoke-type" value="No" v-model="selectedInvokeType">
            <label for="invoke-no">No</label>
        </div>
    </div>

    <div class="year-group">
        <label for="release-year">Release Year:</label>
        <select id="release-year" v-model="selectedRelease">
            <option value="Any">Any</option>
            <option v-for="year in uniqueReleaseYears" :key="year" :value="year">{{ year }}</option>
        </select>
    </div>

    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      selectedTag: '',
      selectedRegion: '',
      selectedGender: '',
      selectedSpecies: '',
      selectedPartype: '',
      selectedRangeType: '',
      selectedRelease: '',
      selectedInvokeType: '',

      species: [
        'Aspect',
        'Brackern',
        'Cat',
        'Celestial',
        'Chemically Altered',
        'Cyborg',
        'Darkin',
        'Demon',
        'Dog',
        'Dragon',
        'God',
        'God-Warrior',
        'Golem',
        'Human',
        'Iceborn',
        'Magically Altered',
        'Magicborn',
        'Minotaur',
        'Rat',
        'Revenant',
        'Spirit',
        'Spiritualist',
        'Troll',
        'Undead',
        'Unknown',
        'Vastayan',
        'Void-Being',
        'Yordle',
      ],
      regions: {
        'Bandle City': 'https://universe.leagueoflegends.com/images/bandle_city_crest_icon.png',
        'Bilgewater': 'https://universe.leagueoflegends.com/images/bilgewater_crest_icon.png',
        'Camavor': 'https://static.wikia.nocookie.net/leagueoflegends/images/8/85/Camavor_Crest_icon.png',
        'Demacia': 'https://universe.leagueoflegends.com/images/demacia_crest_icon.png',
        'Freljord': 'https://universe.leagueoflegends.com/images/freljord_crest_icon.png',
        'Ionia': 'https://universe.leagueoflegends.com/images/iona_crest_icon.png',
        'Ixtal': 'https://universe.leagueoflegends.com/images/ixtal_crest_icon.png',
        'Noxus': 'https://universe.leagueoflegends.com/images/noxus_crest_icon.png',
        'Piltover': 'https://universe.leagueoflegends.com/images/piltover_crest_icon.png',
        'Runeterra': 'https://static.wikia.nocookie.net/leagueoflegends/images/9/94/Runeterra_Crest_icon.png',
        'Shadow Isles': 'https://universe.leagueoflegends.com/images/shadow_isles_crest_icon.png',
        'Shurima': 'https://universe.leagueoflegends.com/images/shurima_crest_icon.png',
        'Targon': 'https://universe.leagueoflegends.com/images/mt_targon_crest_icon.png',
        'Void': 'https://universe.leagueoflegends.com/images/void_crest_icon.png',
        'Zaun': 'https://universe.leagueoflegends.com/images/zaun_crest_icon.png',
      },
      classes: {
        Assassin: 'https://static.wikia.nocookie.net/leagueoflegends/images/2/28/Slayer_icon.png',
        Fighter: 'https://static.wikia.nocookie.net/leagueoflegends/images/8/8f/Fighter_icon.png',
        Mage: 'https://static.wikia.nocookie.net/leagueoflegends/images/2/28/Mage_icon.png',
        Marksman: 'https://static.wikia.nocookie.net/leagueoflegends/images/7/7f/Marksman_icon.png',
        Support: 'https://static.wikia.nocookie.net/leagueoflegends/images/5/58/Controller_icon.png',
        Tank: 'https://static.wikia.nocookie.net/leagueoflegends/images/2/28/Slayer_icon.png',
      },
    };
  },
  computed: {
    
  },
};
</script>

<style scoped>
.container {
  max-width: 100%;
  background-color: #f9f9f9;
}
.filter-group {
  margin-bottom: 20px;
  overflow: auto; /* To handle overflowing content */
}

.filter-group-title {
  display: inline-block;
  width: 120px;
  text-align: right;
  margin-right: 10px;
}

.filter-group-title label {
  font-weight: bold;
}

.class-icons,
.region-icons,
.gender,
.species,
.partype,
.range-type,
.invoke-type,
.year-group {
  display: flex;
  flex-wrap: wrap;
}

.class-icon,
.region-icon,
.gender-value,
.species-value,
.partype-value,
.range-type-value,
.invoke-type-value,
.year-value {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 50px;
  height: 50px;
  margin-right: 10px;
  margin-bottom: 10px;
  border: 1px solid #ccc;
  cursor: pointer;
}

.class-icon img,
.region-icon img {
  width: 100%;
  height: 100%;
}

.selected {
  background-color: blue;
  color: white;
}

/* Force line break for long lists */
.region-group .region-icons {
  flex-wrap: wrap;
}

/* Remove default radio button style */
input[type="radio"] {
  display: none;
}

/* Style the label as clickable */
input[type="radio"] + label {
  display: inline-block;
  width: 50px;
  height: 50px;
  margin-right: 10px;
  margin-bottom: 10px;
  border: 1px solid #ccc;
  cursor: pointer;
  text-align: center;
  line-height: 50px;
}

/* Style the label when selected */
input[type="radio"]:checked + label {
  background-color: blue;
  color: white;
}

.region-icons,
.class-icons {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
}

.region-icon,
.class-icon {
  position: relative;
  margin: 10px;
  cursor: pointer;
  transition: transform 0.3s ease;
}

.region-icon:hover,
.class-icon:hover {
  transform: scale(1.1);
}

.region-icon img,
.class-icon img {
  width: 50px;
  height: 50px;
}

.region-name,
.class-name {
  position: absolute;
  bottom: -20px;
  left: 50%;
  transform: translateX(-50%);
  background-color: rgba(0, 0, 0, 0.7);
  color: white;
  padding: 5px 10px;
  border-radius: 5px;
  font-size: 14px;
  opacity: 0;
  transition: opacity 0.3s ease;
}

</style>

<!-- <style scoped>
.container {
  max-width: 100%;
  padding: 20px;
}

.region-icons,
.class-icons {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
}

.region-icon,
.class-icon {
  position: relative;
  margin: 10px;
  cursor: pointer;
  transition: transform 0.3s ease;
}

.region-icon:hover,
.class-icon:hover {
  transform: scale(1.1);
}

.region-icon img,
.class-icon img {
  width: 50px;
  height: 50px;
}

.region-name,
.class-name {
  position: absolute;
  bottom: -20px;
  left: 50%;
  transform: translateX(-50%);
  background-color: rgba(0, 0, 0, 0.7);
  color: white;
  padding: 5px 10px;
  border-radius: 5px;
  font-size: 14px;
  opacity: 0;
  transition: opacity 0.3s ease;
}

.filter-group {
  margin-bottom: 15px;
}

.filter-group label {
  font-weight: bold;
  margin-bottom: 5px;
  display: block;
}

.region-icon:hover .region-name,
.class-icon:hover .class-name {
  opacity: 1;
}


/* Title styling */
.gender-group label,
.species-group label,
.resource-group label,
.range-group label,
.invoke-group label,
.year-group label {
  display: inline-block;
  width: 100px; /* Adjust width as needed */
}

/* Radio button styling - hiding them */
.gender-group input[type="radio"],
.resource-group input[type="radio"],
.range-group input[type="radio"],
.invoke-group input[type="radio"] {
  display: none;
}

/* Styling the value boxes */
.gender-group input[type="radio"] + label,
.resource-group input[type="radio"] + label,
.range-group input[type="radio"] + label,
.invoke-group input[type="radio"] + label {
  display: inline-block;
  padding: 5px 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  cursor: pointer;
}

/* Styling the selected value box */
.gender-group input[type="radio"]:checked + label,
.resource-group input[type="radio"]:checked + label,
.range-group input[type="radio"]:checked + label,
.invoke-group input[type="radio"]:checked + label {
  background-color: blue;
  color: white;
}


</style> -->