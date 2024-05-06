<template>
  <div class="filter-container">
    <input v-model="searchQuery" placeholder="Filter by Name" />

    <div>
      <label>Champion Class:</label>
      <select v-model="selectedRole">
        <option value="">All</option>
        <option value="Fighter">Fighter</option>
        <option value="Assassin">Assassin</option>
        <option value="Mage">Mage</option>
        <option value="Marksman">Marksman</option>
        <option value="Support">Support</option>
        <option value="Tank">Tank</option>
      </select>
    </div>

    <div class="partype">
      <label for="mana">Mana</label>
      <input type="radio" id="mana" class="partype-radio" name="partype" value="Mana" />
      <label for="no-mana">No Mana</label>
      <input type="radio" id="no-mana" class="partype-radio" name="partype" value="No Mana" />
      <div class="slider"></div>
    </div>



    <div>
      <label>Region:</label>
      <select v-model="selectedRegion">
        <option value="">All</option>
        <option value="Piltover">Piltover</option>
        <option value="Demacia">Demacia</option>
        <!-- Add options for other regions -->
      </select>
    </div>

    <div>
      <label>Attack:</label>
      <div>
        <input type="radio" id="melee" name="attack" value="Melee" />
        <label for="melee">Melee</label>
      </div>
      <div>
        <input type="radio" id="ranged" name="attack" value="Ranged" />
        <label for="ranged">Ranged</label>
      </div>
      <div>
        <input type="radio" id="mixed-attack" name="attack" value="Mixed" />
        <label for="mixed-attack">Mixed</label>
      </div>
    </div>

    <div>
      <label>Release Year:</label>
      <input type="number" v-model="selectedRelease" min="2009" max="2023" />
    </div>

    <div>
      <label>Can Invoke Entity:</label>
      <div>
        <input type="radio" id="can-invoke-yes" name="can-invoke" value="true" />
        <label for="can-invoke-yes">Yes</label>
      </div>
      <div>
        <input type="radio" id="can-invoke-no" name="can-invoke" value="false" />
        <label for="can-invoke-no">No</label>
      </div>
    </div>

    <div>
      <label>Champion Race:</label>
      <div>
        <input type="radio" id="ascended" name="race" value="Ascended" />
        <label for="ascended">Ascended</label>
      </div>
      <div>
        <input type="radio" id="yordle" name="race" value="Yordle" />
        <label for="yordle">Yordle</label>
      </div>
      <!-- Add similar radio buttons for other races -->
    </div>
  </div>
</template>

<script>
import championsData from '@/data/champions.json';

export default {
  data() {
    return {
      champions: Object.values(championsData),
      searchQuery: '',
      selectedTag: '',
      selectedPartype: '',
      selectedRegion: '',
      selectedAttack: '',
      selectedRelease: '',
      selectedCanInvoke: '',
      selectedRole: '',
      selectedRace: '',
    };
  },
  computed: {
    uniqueTags() {
      return [...new Set(this.champions.flatMap(champion => champion.tags))];
    },
    uniquePartypes() {
      return [...new Set(this.champions.map(champion => champion.partype))];
    },
    uniqueRegions() {
      return [...new Set(this.champions.map(champion => champion.region))];
    },
    uniqueRoles() {
      return [...new Set(this.champions.flatMap(champion => champion.roles))];
    },
    uniqueRaces() {
      return [...new Set(this.champions.flatMap(champion => champion.races))];
    },
    uniqueReleaseYears() {
      return [...new Set(this.champions.map(champion => champion.release))];
    },
    filteredChampions() {
      return this.champions.filter(champion => {
        const matchesName = champion.name.toLowerCase().includes(this.searchQuery.toLowerCase());
        const matchesTag = !this.selectedTag || champion.tags.includes(this.selectedTag);
        const matchesPartype = !this.selectedPartype || champion.partype === this.selectedPartype;
        const matchesRegion = !this.selectedRegion || champion.region === this.selectedRegion;
        const matchesAttack = !this.selectedAttack || champion.attack === this.selectedAttack;
        const matchesRelease = !this.selectedRelease || champion.release.toString() === this.selectedRelease;
        const matchesCanInvoke = !this.selectedCanInvoke || champion.can_invoke.toString() === this.selectedCanInvoke;
        const matchesRole = !this.selectedRole || champion.roles.includes(this.selectedRole);
        const matchesRace = !this.selectedRace || champion.races.includes(this.selectedRace);

        return (
          matchesName &&
          matchesTag &&
          matchesPartype &&
          matchesRegion &&
          matchesAttack &&
          matchesRelease &&
          matchesCanInvoke &&
          matchesRole &&
          matchesRace
        );
      });
    },
  },
};
</script>

<style scoped>
/* .filter-container {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}

.filter-container>div {
  flex: 1;
  min-width: 150px;
  margin-bottom: 10px;
} */

.partype {
  display: flex;
  align-items: center;
  position: relative;
}

.partype label {
  margin-right: 20px;
  /* Adjust spacing as needed */
  cursor: pointer;
}

.partype-radio {
  display: none;
}

.slider {
  position: absolute;
  width: 40px;
  /* Width of the circle */
  height: 40px;
  /* Height of the circle */
  background-color: #007bff;
  /* Color of the circle */
  border-radius: 50%;
  /* Make it a circle */
  transform: translateX(0);
  /* Initial position at the first option */
  transition: transform 0.3s ease;
  /* Smooth sliding animation */
}

#mana:checked~.slider {
  transform: translateX(0);
  /* Position it over the first option */
}

#no-mana:checked~.slider {
  transform: translateX(60px);
  /* Position it over the second option */
}</style>