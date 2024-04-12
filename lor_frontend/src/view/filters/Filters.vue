<template>
  <div class="grid items-center justify-center">
    <div class="flex items-center">
    <!-- Add 5 small images here -->
      <div class="flex items-center space-x-1">
        <img src="" class="h-6 w-6 rounded-full" alt="Image 1">
        <img src="" class="h-6 w-6 rounded-full" alt="Image 2">
        <img src="" class="h-6 w-6 rounded-full" alt="Image 3">
        <img src="" class="h-6 w-6 rounded-full" alt="Image 4">
        <img src="" class="h-6 w-6 rounded-full" alt="Image 5">
      </div>
      <!-- End of small images -->
      <div class="relative">
        <div class="absolute inset-y-0 left-0 flex items-center pl-3">
          <svg class="h-5 w-5 text-gray-400 dark:text-gray-500" fill="currentColor" viewBox="0 0 20 20">
          </svg>
        </div>
        <input type="text" class="border border-gray-300 dark:border-gray-700 rounded-md pl-4 pr-4 py-2 focus:outline-none focus:border-blue-500 dark:bg-gray-800 dark:text-white" placeholder="Champion name..." @input="emitInput">
      </div>
      <button @click="selectAll" class="ml-4 bg-gray-200 dark:bg-gray-700 hover:bg-gray-300 dark:hover:bg-gray-600 text-gray-700 dark:text-white font-bold py-1 px-3 rounded">
        Select All
      </button>
      <button @click="unselectAll" class="ml-2 bg-gray-200 dark:bg-gray-700 hover:bg-gray-300 dark:hover:bg-gray-600 text-gray-700 dark:text-white font-bold py-1 px-3 rounded">
        Unselect All
      </button>
    </div>
    <div class="flex items-center justify-center">
      <button @click="generate" class="mt-4 bg-blue-500 dark:bg-blue-700 hover:bg-blue-600 dark:hover:bg-blue-800 text-white font-bold py-2 px-2 rounded w-32">
        GENERATE
      </button>
    </div>
  </div>
  <AdvancedFilters ref="advancedFilters" @update-filter="updateFilter" />
</template>

<script>
import AdvancedFilters from '../filters/AdvancedFilters.vue'

export default {
  name: 'GenerateRandomChampion',
  emits: ['update-filter', 'input-change', 'select-all', 'unselect-all', 'generate'],
  components: {
    AdvancedFilters
  },
  methods: {
    emitInput(event) {
      this.$emit('input-change', event.target.value);
    },
    selectAll() {
      this.$emit('select-all');
    },
    unselectAll() {
      this.$emit('unselect-all');
    },
    generate(filters) {
      this.$emit('generate', filters);
    },
    updateFilter(filter) {
      this.$emit('update-filter', filter);
    }
  }
}
</script>

<style scoped>
/* Your style goes here */
</style>
