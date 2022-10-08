<template>
  <div>
    <div class="level">
      <div class="level-left">
        <p class="level-item">
          <span class="is-size-5 has-text-weight-semibold">Basic Master</span>
        </p>
      </div>
      <div class="level-right"></div>
    </div>

    <b-tabs>
      <b-tab-item label="Colour"> <colour /> </b-tab-item>
      <b-tab-item label="Craft Category"></b-tab-item>
      <b-tab-item label="Fabric"></b-tab-item>
      <b-tab-item label="Tags"></b-tab-item>
    </b-tabs>
    <!-- <b-loading
      :is-full-page="true"
      :active.sync="submitLoad"
      :can-cancel="false"
    ></b-loading> -->
  </div>
</template>


<script>
import Colour from "../components/colour.vue";

export default {
  components: {
    Colour,
  },
  data() {
    return {};
  },
};
</script>

<style>
.noti-x {
  border: 1px solid lightblue;
  border-top: 5px solid lightblue;
  border-radius: 0 0 10px 10px;
  background-color: #fff;
}
</style>