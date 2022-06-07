<template>
  <div class>
    <div class="level">
      <div class="level-left">
        <p class="level-item">
          <span class="title is-size-4">Settings</span>
        </p>
      </div>
      <div class="level-right"></div>
    </div>

    <div class="box box-x">
      <label for class="label">
        Shopify Shop Name
        <b-tag>myshop.myshopify.com</b-tag>
      </label>
      <b-input v-model="shopname" placeholder="myshop" />
      <br />
      <label for class="label">Shopify API URL</label>
      <b-input v-model="shopurl" placeholder="Enter Shopify URI" />

      <br />
      <button class="button is-link" @click="updateShop">
        <b-icon class="mr-3" icon="check" />
        <span> Save </span>
      </button>
    </div>
    <div class="box box-x">
      <p class="is-size-5 has-text-weight-bold">
        <span class="bullet"></span>
        Invoice Settings
      </p>
      <hr class="my-3 has-background-light" />
      <p for class="mb-4 heading">Sender</p>

      <b-field label="Uploaded Logo">
        <img :src="'/uploads/' + logopath" style="height: 50px" alt="" />
      </b-field>
      <label class="label ">Firm Logo</label>
      <b-field
        class="file is-primary"
        name="firm_logo"
        :class="{ 'has-name': !!file }"
      >
        <b-upload v-model="logofile" class="file-label">
          <span class="file-cta">
            <b-icon class="file-icon" icon="upload"></b-icon>
            <span class="file-label">Click to upload</span>
          </span>
          <span class="file-name" v-if="file">
            {{ file.name }}
          </span>
        </b-upload>
      </b-field>
      <b-field class="is-grouped is-group-multiline">
        <b-field label="Firm Name">
          <b-input v-model="firm.name" placeholder="Firm Name"></b-input>
        </b-field>

        <b-field label="Phone">
          <b-input placeholder="Phone" v-model="firm.phone"></b-input>
        </b-field>
        <b-field class="is-expanded" label="GSTIN">
          <b-input placeholder="GSTIN" v-model="firm.gst"></b-input>
        </b-field>
      </b-field>
      <b-field label="Address">
        <b-input
          type="textarea"
          placeholder="Address"
          v-model="firm.address"
        ></b-input>
      </b-field>
      <b-field class="is-grouped">
        <b-field label="Order No. Start">
          <b-input
            icon="pound-box"
            placeholder="Starting Order No."
            v-model="firm.order_start"
          ></b-input>
        </b-field>
      </b-field>

      <button class="button is-link" @click="updateFirm">
        <b-icon class="mr-3" icon="check" />
        <span> Save </span>
      </button>
    </div>
  </div>
</template>


<script>
export default {
  data() {
    return {
      firm: {
        name: null,
        gst: null,
        address: null,
        phone: null,
        order_start: null,
      },
      logofile: null,
      logopath: null,
      shopurl: this.$auth.user.shop_url,
      shopname: this.$auth.user.shop_name,
    };
  },
  mounted() {
    let self = this;
    this.$axios.get("get/user/firm").then((response) => {
      this.firm.name = response.data.firm_name;
      this.firm.gst = response.data.firm_gst;
      this.firm.phone = response.data.firm_phone;
      this.firm.address = response.data.firm_address;
      this.firm.order_start = response.data.order_start;
      this.logopath = response.data.image;
    });
  },
  methods: {
    updateShop() {
      let self = this;
      this.$axios
        .post("/update/user", {
          shop_url: this.shopurl,
          shop_name: this.shopname,
        })
        .then((response) => {
          if (response.data.success) {
            self.$buefy.snackbar.open({
              duration: 4000,
              message: response.data.success,
              type: "is-light",
              position: "is-top-right",
              actionText: "Close",
              queue: true,
              onAction: () => {
                self.isActive = false;
              },
            });
          }
          if (response.data.message) {
            self.$buefy.snackbar.open({
              duration: 4000,
              message: response.data.message,
              type: "is-light",
              position: "is-top-right",
              actionText: "Close",
              queue: true,
              onAction: () => {
                self.isActive = false;
              },
            });
          }
        });
    },
    updateFirm() {
      let self = this;
      let payload = new FormData();
      payload.append("data", JSON.stringify({ firm: this.firm }));
      payload.append("files", this.logofile);
      this.$axios
        .post("/update/user/firm", payload, {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        })
        .then((response) => {
          if (response.data.success) {
            self.$buefy.snackbar.open({
              duration: 4000,
              message: response.data.success,
              type: "is-light",
              position: "is-top-right",
              actionText: "Close",
              queue: true,
              onAction: () => {
                self.isActive = false;
              },
            });
          }
          if (response.data.message) {
            self.$buefy.snackbar.open({
              duration: 4000,
              message: response.data.message,
              type: "is-light",
              position: "is-top-right",
              actionText: "Close",
              queue: true,
              onAction: () => {
                self.isActive = false;
              },
            });
          }
        });
    },
  },
};
</script>
<style>
.accent-bk {
  background-color: #0a0a0a;
  position: absolute;
  top: 0;
  left: 0;
  z-index: -1;
  width: 100%;
  height: 200px;
  transform: translateY(-50px);
}

.box-x {
  /* box-shadow:  none !important; */
  /* border: 2px solid #cecece; */
  border-radius: 10px;
}

.bullet {
  display: inline-block;
  width: 10px;
  height: 10px;
  background-color: blue;
  opacity: 0.6;
  margin-bottom: 3px;
  margin-right: 5px;
  border-radius: 50%;
}
</style>