<template>
  <div class="mt-5">
    <!-- Edit Modal -->
    <b-modal :active.sync="modal">
      <div class="card">
        <div class="card-content">
          <div class="content">
            <p class="has-text-weight-bold is-size-5">Edit Data</p>
            <div class="control">
              <b-field label="Data" :type="{'is-danger': edit.errors.name}">
                <b-input v-model="edit.name" ref="editname" placeholder="Enter Data" />
              </b-field>
             
            </div>
          </div>
        </div>
        <footer class="card-footer">
          <a class="card-footer-item" @click.prevent="saveEditData">
            <b-icon icon="refresh" class="mr-3"></b-icon>
            <span>Update</span>
          </a>
          <a class="card-footer-item has-text-grey" @click.prevent="modal = !modal">
            <b-icon class="mr-3" icon="close"></b-icon>
            <span>Close</span>
          </a>
        </footer>
      </div>
    </b-modal>

    <!-- Entry Form -->
    <div class="box" v-show="view">
      <form id="data_entry" class="animated fadeIn" novalidate="true" @submit="submitData ;">
        <div class="columns">
          <div class="column">
            <div class="control">
              <b-field label="Data" :type="{'is-danger': form.errors.name}">
                <b-input
                  expanded
                  type="text"
                  v-model="form.name"
                  ref="name"
                  placeholder="Enter Data"
                />
              </b-field>
            
            </div>
            <br />
            <div class="field is-grouped">
              <div class="control">
                <button type="submit" @click.prevent="submitData" class="button is-link">
                  <b-icon class="mr-3" icon="check"></b-icon>
                  <span>Save</span>
                </button>
              </div>
              <div class="control">
                <button class="button" @click.prevent="view = !view ;getData()">
                  <b-icon class="mr-3" icon="eye"></b-icon>
                  <span>View</span>
                </button>
              </div>
              <span
                class="button is-danger is-light is-underline"
                v-if="Object.keys(form.errors).length != 0"
              >
                <b-icon icon="error"></b-icon>
                <span>Please Fix Errors</span>
              </span>
            </div>
          </div>
        </div>
      </form>
    </div>

    <!-- Table  -->

    <div v-show="!view">
      <div class="control">
        <button class="button is-link" @click.prevent="view = !view ;">
          <b-icon icon="plus" class="mr-3"></b-icon>
          <span>Add</span>
        </button>
      </div>
      <br />
      <div>
        <b-loading :active.sync="loading"></b-loading>
        <div
          v-if="loading_set && data.length == 0"
          class="has-text-grey-lighter has-text-centered pt-6"
        >
          <b-icon icon="file-plus" size="is-large"></b-icon>
          <br />
          <p class="is-size-5 has-text-weight-semibold">
            Nothing to show.
            <br />Add some data
          </p>
        </div>

        <div class="box" v-else>
        <b-field class="mb-4">
            <b-input
              icon="magnify"
              placeholder="Search "
              v-model="query_search"
            ></b-input>
          </b-field>
          <b-table :data="autocompleteData">
            <template>
              <b-table-column v-slot="props" field="name" label="Name">{{props.row.name}}</b-table-column>
              <b-table-column v-slot="props" field label="More">
                <div class="buttons">
                  <button @click.prevent="editData(props.row ,props.row.id)" class="button">Edit</button>
                  <button @click="deleteData(props.row, props.index)" class="button is-danger is-light">
                    <b-icon icon="delete"></b-icon>
                  </button>
                </div>
              </b-table-column>
            </template>
          </b-table>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  layout: "admin",
  data() {
    return {
      view: true,
      form: {
        errors: {},
        id: null,
        name: null,
     
      },
      isSubmitting: false,
      data: [],
      loading: false,
      loading_set: false,
      modal: false,
      edit: {
        errors: {},
        name: null,
       
        index: null,
      },
      query_search: "",
    };
  },
computed:{
      autocompleteData() {
      if (this.data.length != 0) {
        if (this.query_search == "") {
          return this.data;
        } else {
          return this.data.filter((option) => {
            return (
              option.name
                .toString()
                .toLowerCase()
                .indexOf(this.query_search.toLowerCase()) >= 0
            );
          });
        }
      }
    },
  },
  mounted() {
    this.$refs.name.focus();
  },
  methods: {
    checkData(e) {
      this.form.errors = {};

      if (this.form.name) {
        return true;
      }
      if (!this.form.name) {
        this.$set(this.form.errors, "name", true);
      }
    },

   
    submitData(e) {
      let self = this;
      this.isSubmitting = true;
      if (this.checkData()) {
        this.$axios
          .post("/add/craft", this.form)
          .then(function (response) {
            self.isSubmitting = false;
            if (response.data.success) {
              self.form.name = null;
           

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
            } else {
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
            }
          })
          .catch(function (error) {
            self.isSubmitting = false;
            console.log(error);
            self.$buefy.snackbar.open({
              duration: 4000,
              message: "Unable to save Data",
              type: "is-light",
              position: "is-top-right",
              actionText: "Close",
              queue: true,
              onAction: () => {
                self.isActive = false;
              },
            });
          });
      }
    },
    getData(e) {
      let self = this;
      this.loading = true;
      this.$axios
        .get("/get/craft")
        .then(function (response) {
          self.data = response.data;
        })
        .catch(function (error) {
          this.loading = false;
          self.$buefy.snackbar.open({
            duration: 4000,
            message: "Unable to fetch data",
            type: "is-light",
            position: "is-top-right",
            actionText: "Close",
            queue: true,
            onAction: () => {
              self.isActive = false;
            },
          });
        })
        .finally(() => {
          this.loading = false;
          this.loading_set = true;
        });
    },
    editData(data, index) {
      this.edit.errors = {};

      this.modal = true;
      this.edit.name = data.name;
      this.edit.id = data.id;
      this.edit.index = index;
    },
    saveEditData(e) {
      let self = this;
      let dataList = this.data;
      this.edit.errors = {};

      if (this.edit.name) {
        this.$axios
          .post("/edit/craft", this.edit)
          .then(function (response) {
            if (response.data.success) {
              dataList = self.data.filter(function (x) {
                return x.id === self.edit.id;
              });
              dataList[0].name = self.edit.name;
              self.modal = !self.modal;

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
            } else {
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
            }
          })
          .catch(function (error) {
            console.log(error);
            if (response.data.message) {
              self.$buefy.snackbar.open({
                duration: 4000,
                message: "Unable to save data",
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
        return true;
      }

      if (!this.edit.name) {
        this.$set(this.edit.errors, "name", true);
      }
    },
    deleteData(data, index) {
      let dataList = this.data;
      let self = this;
      this.$axios
        .post("/delete/craft", data)
        .then(function (response) {
          if (response.data.success) {
            dataList.splice(index, 1);
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
          } else {
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
        })
        .catch(function (error) {
          console.log(error);
          self.$buefy.snackbar.open({
            duration: 4000,
            message: "Unable to delete Data",
            type: "is-light",
            position: "is-top-right",
            actionText: "Close",
            queue: true,
            onAction: () => {
              self.isActive = false;
            },
          });
        });
    },
  },
};
</script>