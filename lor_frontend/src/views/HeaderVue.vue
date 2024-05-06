<template>
  <header class="page-header">
    <div class="logo">
      <img src="../assets/challenger_icon.png" alt="Logo" />
    </div>
    <nav class="nav-links">
      <router-link to="/">Home</router-link>
      <router-link to="/about">About</router-link>
      <router-link to="/contact">Contact</router-link>
    </nav>
  </header>
</template>

<style scoped>
.page-header {
  background-color: #333;
  color: #fff;
  padding: 10px 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo img {
  width: 50px;
  /* Adjust the size of the logo as needed */
}

.nav-links router-link {
  color: #fff;
  text-decoration: none;
  margin-left: 20px;
}

.nav-links a:hover {
  text-decoration: underline;
}
</style>
