<template>
  <div>
    <nav class="navbar">
      <div class="container">
        <div class="navbar-brand">
          <p class="navbar-item is-size-5 has-text-weight-light">
            STORE | FRONT
          </p>
        </div>
        <div class="navbar-end">
          <nuxt-link to="/products" class="navbar-item">
            <span class="icon icon-btn">
              <feather type="package" size="1.3rem" />
            </span>
            Products
          </nuxt-link>
          <nuxt-link to="/new" class="navbar-item">
            <span class="icon icon-btn">  
              <feather type="plus-square" size="1.3rem" />
            </span>
            New
          </nuxt-link>
          <nuxt-link to="/master" class="navbar-item">
            <span class="icon icon-btn">
              <feather type="grid"  size="1.3rem"/>
            </span>
            Master
          </nuxt-link>
        </div>
      </div>
    </nav>
    <section class="section">
      <div class="container">
        <nuxt />
      </div>
    </section>
  </div>
</template>

<style>
body {
  font-family: "Inter", "Roboto", "Helvetica", "Segoe UI", sans-serif;
}

.icon-btn {
  margin: 0 5px 1px 5px !important;
  vertical-align: middle !important;
}
</style>