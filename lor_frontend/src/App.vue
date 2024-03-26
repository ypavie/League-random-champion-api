<template>
  <!-- <HeaderVue />
  <div class="main-container">
    <div class="left-container">
        <SelectedChampionVue :champion="selectedChampion" />
    </div>
    <div class="right-container">
      <ChampionListVue />
    </div>
  </div> -->
  <UIView />
</template>

<script>
// import FilterVue from './views/FilterVue.vue'
// import SelectedChampionVue from './views/SelectedChampionVue.vue'
// import ChampionListVue from './views/ChampionListVue.vue'
// import HeaderVue from './views/HeaderVue.vue'
import UIView from './views/UIView.vue'

export default {
  components: {
    // FilterVue,
    // ChampionListVue,
    // SelectedChampionVue,
    // HeaderVue,
    UIView
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
img {
  border-radius: 8px;
}


</style>
