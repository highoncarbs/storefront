<template>
  <div>
    <div v-for="(or, o_index) in order" class="pagebreak" :key="'order_' + o_index">
      <div>
        <div class="level">
          <div class="level-left">
            <div class="level-item">
              <figure class="image my-5">
                <img
                  class="container"
                  :src="'/uploads/' + logopath"
                  style="width: 150px"
                  alt=""
                />
              </figure>
            </div>
          </div>
          <div class="level-right">
            <div class="level-item">
              <div class="has-text-black">
                <p class="has-text-weight-bold is-capitalized" v-if="order">
                  {{ or.customer.first_name }} {{ or.customer.last_name }}
                </p>
                <p class="has-text-weight-bold" v-if="or">{{ or.name }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div v-if="or">
        <div class="columns is-multiline">
          <div
            class="column is-3"
            v-for="(row, index) in or.line_items"
            :key="index"
          >
            <figure class="image is-3by4">
              <img :src="row.image" alt="" />
            </figure>
            <div class="is-size-6">
              <p class="">
                <span class="has-text-weight-semibold has-text-grey">
                  {{ index + 1 }}.
                </span>
                {{ row.title }}
              </p>

              <p>
                <span class="has-text-weight-bold"> QTY </span>
                - {{ row.quantity }}
              </p>
            </div>
          </div>
          <!-- <div class="column"></div>
      <div class="column"></div>
      <div class="column"></div> -->
        </div>
      </div>
      <div v-else>
        <div class="section container has-text-centered">
          <!-- <b-icon icon=""></b-icon> -->
          <p class="is-size-2 title has-text-weight-semibold">Please wait</p>
          <p class="is-size-3 subtitle has-text-weight-semibold has-text-grey">
            Loading order images
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  layout: "empty",
  data() {
    return {
      logopath: null,
      order: null,
      order_img: [],
      firm: {
        name: null,
        gst: null,
        address: null,
        phone: null,
        order_start: null,
      },
      logopath: null,
    };
  },
  mounted() {
    this.$axios.get("get/user/firm").then((response) => {
      this.firm.name = response.data.firm_name;
      this.firm.gst = response.data.firm_gst;
      this.firm.phone = response.data.firm_phone;
      this.firm.address = response.data.firm_address;
      this.firm.order_start = response.data.order_start;
      this.logopath = response.data.image;
    });
    this.order = JSON.parse(localStorage.getItem("order-img-list"));
    this.order.forEach((item, m_index) => {
      item.line_items.forEach((row, index) => {
        this.getProduct(row.product_id, index, m_index);
      });
    });
  },
  methods: {
    getProduct(id, index, m_index) {
      let self = this;
      this.$axios.get(`/product/${id}`).then((response) => {
        console.log(id, response.data.images)
        // try {
        //   let image_src = response.data.images[0].src;
        //   self.order[m_index].line_items[index].image = image_src;
        //   //   this.order_img.push({ image_src, index });
        //   setTimeout(function () {}, 1500);
        //   // console.log("~", image_src);
        //   return image_src;
        // } catch (error) {
        //   console.log(error);
        //   return null;
        // }
      });
    },
  },
};
</script>

<style>
@media print {
    .pagebreak { page-break-before: always; } /* page-break-after works, as well */
}
</style>