<template>
  <div class="champion-list-vue">
    <div class="champion-icons">
      <div v-for="(champion, championName) in getChampionToDisplay()" 
      :key="champion.id" 
      class="champion-icon">
        <img :src="champion.icon"
          @click="banChampion(championName)"
          :class="{ selected: bannedChampions.includes(championName) }" 
        />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      currentPatch: '14.6.1',
      searchTerm: '',
      bannedChampions: [],
      filteredChampions: {}
    }
  },
  props: {
    champions: Object,
  },
  mounted() {
    this.filteredChampions = this.champions;
  },
  watch: {
    champions: {
      handler(newChampions) {
        this.filteredChampions = newChampions;
      },
      deep: true
    }
  },
  methods: {
    getChampionToDisplay() {
      const championsToDisplay = {};
      for (const championName in this.champions) {
        if (this.filteredChampions[championName]) {
          championsToDisplay[championName] = this.champions[championName];
        }
      }
      return championsToDisplay;
    },
    banChampion(championName) {
      if (this.bannedChampions.includes(championName)) {
        this.bannedChampions = this.bannedChampions.filter(champion => champion !== championName);
      } else {
        this.bannedChampions.push(championName);
      }
      this.$emit('bannedChampions', this.bannedChampions);
    },
    updateBanlist(champions) {
      this.bannedChampions = Object.keys(champions);
    },
    updateFilteredlist(champions) {
      this.filteredChampions = champions
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
  width: 100%;
  align-items: flex-end;
}

.champion-icon {
  text-align: center;
}

.champion-icon img {
  width: 65px;
  height: 65px;
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

.filter-input {
  display: flex;
  justify-content: space-between;
}
</style>
