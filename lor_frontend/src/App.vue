<template>
  <HeaderVue />
  <div class="main-container">
    <div class="left-third">
      <div class="filters">
        <FilterVue />
      </div>
      <div class="selected-champion">
        <SelectedChampionVue :champion="selectedChampion" />
      </div>
    </div>
    <div class="right-two-thirds">
      <ChampionListVue />
    </div>
  </div>
</template>

<script>
import FilterVue from './views/FilterVue.vue'
import ChampionListVue from './views/ChampionListVue.vue'
import SelectedChampionVue from './views/SelectedChampionVue.vue'
import HeaderVue from './views/HeaderVue.vue'

export default {
  components: {
    FilterVue,
    ChampionListVue,
    SelectedChampionVue,
    HeaderVue
  },
  data() {
    return {
      selectedChampion: null,
      dataLoading: true
    }
  },
  created() {
    // Start the async call to the backend URL when the component is created
    this.fetchData();
    console.log('App.vue created');
  },
  methods: {
    fetchData() {
      const currentUrl = window.location.href;
      const url = new URL(currentUrl);
      const pathSegments = url.pathname.split('/');
      const id = pathSegments.pop(); // Get the last segment from the path
      if (id === '') return;

      this.updateSelectedChampion(id);
    },
    async updateSelectedChampion(id) {
      try {
        const response = await fetch(`http://localhost:8000/champion/${id}`);
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        const data = await response.json();
        this.selectedChampion = data;
        console.log('Selected champion:', this.selectedChampion);
      } catch (error) {
        console.error('Error fetching data:', error);
        this.dataLoading = false; // Handle errors by setting dataLoading to false
      }
    }
  },

}
</script>

<style>
.main-container {
  display: flex;
  flex-direction: row;
  height: 100vh;
  width: 100%;
}

.left-third {
  flex: 2;
  display: flex;
  flex-direction: column;
}

/* .left-third .filters {
  height: 50%;
}

.left-third .selected-champion {
  height: 50%;
} */

.right-two-thirds {
  flex: 1;
  overflow-y: auto;
}
</style>
