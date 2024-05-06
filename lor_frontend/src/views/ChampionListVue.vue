<template>
  <div class="champion-list-vue">
    <!-- Search Bar -->
    <div class="search-bar">
      <input v-model="searchTerm" type="text" placeholder="Search by name..." @input="filterChampions" />
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
      searchTerm: '',
      champions: championsData,
      bannedChampions: []
    }
  },
  methods: {
    banChampion(championName) {
      // if (this.bannedChampions.includes(championName)) {
      //   this.bannedChampions = this.bannedChampions.filter(name => name !== championName)
      // } else {
      //   this.bannedChampions.push(championName)
      // }
      console.log('banChampion')
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
        if (champion.name.toLowerCase().includes(normalizedSearchTerm) && !this.bannedChampions.includes(championName)) {
          filtered[championName] = champion
        }
        return filtered
      }, {})
    },
  },
  methods: {
    filterChampions() { }
  }
}
</script>

<style>
.champion-list-vue {
  padding: 5px;
}

.search-bar {
  text-align: center;
  margin: 10px 0;
}

input[type='text'] {
  width: 80%;
  font-size: 16px;
}

.champion-icons {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}

.champion-icon {
  text-align: center;
}

.champion-icon img {
  width: 75px;
  height: 75px;
}

.champion-icon img:hover {
  cursor: pointer;
}

.champion-icon img:active {
  transform: scale(0.9);
}

.champion-icon:hover:not(.selected) {
  filter: brightness(155%);
}

.selected {
  filter: grayscale(100%);
}
</style>
