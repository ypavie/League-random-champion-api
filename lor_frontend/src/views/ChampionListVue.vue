<template>
  <div class="champion-list-vue">
    <!-- Search Bar -->
    <div class="search-bar">
      <div class="filter-input">
        <div>Current patch: {{ currentPatch }}</div>
        <input v-model="searchTerm" type="text" placeholder="Search by name..." @input="filterChampions" />
        <div>
          <img class="filter-btn" src="https://ddragon.leagueoflegends.com/cdn/11.16.1/img/champion/Aatrox.png" />
          <img class="filter-btn" src="https://ddragon.leagueoflegends.com/cdn/11.16.1/img/champion/Aatrox.png" />
          <img class="filter-btn" src="https://ddragon.leagueoflegends.com/cdn/11.16.1/img/champion/Aatrox.png" />
        </div>
      </div>
    </div>


    <!-- Display Filtered Icons -->
    <div class="champion-icons">
      <div v-for="(champion, championName) in filteredChampions" :key="champion.id" class="champion-icon">
        <img :src="champion.icon"
          @click="bannedChampions.includes(championName) ? bannedChampions.splice(bannedChampions.indexOf(championName), 1) : bannedChampions.push(championName)"
          :class="{ selected: bannedChampions.includes(championName) }" />
      </div>
    </div>
  </div>
</template>

<script>
import championsData from '@/data/champions.json'
export default {
  data() {
    return {
      currentPatch: '14.6.1',
      searchTerm: '',
      champions: championsData,
      bannedChampions: []
    }
  },
  methods: {
    banChampion(championName) {
      if (this.bannedChampions.includes(championName)) {
        this.bannedChampions = this.bannedChampions.filter(name => name !== championName)
      } else {
        this.bannedChampions.push(championName)
      }
    }
  },
  computed: {
    filteredChampions() {
      const normalizedSearchTerm = this.searchTerm.toLowerCase().trim()
      if (normalizedSearchTerm === '') {
        return this.champions
      }
      return Object.keys(this.champions).reduce((filtered, championName) => {
        const champion = this.champions[championName]
        if (champion.name.toLowerCase().includes(normalizedSearchTerm)) {
          filtered[championName] = champion
        }
        return filtered
      }, {})
    },
  },
}
</script>

<style scoped>

.champion-list-vue {
  padding: 5px;
}

.search-bar {
  text-align: center;
  margin-left: 10px;
  margin-top: 10px;
}

input[type='text'] {
  width: 50%;
  font-size: 18px;
  text-transform: uppercase;
  font-weight: bold;
  height: 40px;
}

.champion-icons {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  max-height: 85vh;
  overflow-y: auto;
  width: 100%;
  align-items: flex-end;
}

.champion-icon {
  text-align: center;
}

.champion-icon img {
  width: 75px;
  height: 75px;
  margin: 1px;
}

.champion-icon img:hover {
  cursor: pointer;
  transform: scale(1.1);
}

.champion-icon img:active {
  transform: scale(0.9);
}

.champion-icon img:hover:not(.selected) {
  filter: brightness(140%);
}

.selected {
  filter: grayscale(100%) brightness(30%);
}

.filter-btn {
  width: 30px;
  height: 30px;
  margin: 5px;
  cursor: pointer;
}

.filter-btn:hover {
  transform: scale(1.1);
}

.filter-btn:active {
  transform: scale(0.9);
}

/* I want the current patch on left, the other on right */
.filter-input {
  display: flex;
  justify-content: space-between;
}
</style>
