<template>
  <div>
    <div class="level">
      <div class="level-left">
        <p class="level-item">
          <span class="title">New Master</span>
        </p>
      </div>
      <div class="level-right"></div>
    </div>
    <br />
    <div class="box">
      <label for class="label">Shopify API URL</label>
      <input type="text" class="input" placeholder="Enter Shopify URI" />
      <br />
      <br />
      <button class="button is-info">
          <b-icon class="icon-btn" icon="check" />
          Save
      </button>
    </div>
  </div>
</template>


<script>
import axios from "axios";

export default {
  data() {
    return {
      products: [],
      loading: true
    };
  },
  mounted() {
    let self = this;
  },
  methods: {}
};
</script>