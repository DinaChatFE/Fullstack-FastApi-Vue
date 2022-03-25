import axios from "axios";

const baseLink = process.env.VUE_APP_API;

export default {
  getProductApi: cb => {
    setTimeout(() => {
      axios.get(baseLink + "/data?_sort=created_at&_order=desc").then(res => {
        cb(res);
      });
    }, 1000);
  },
  addNewProductApi: (product, cb) => {
    axios.post(baseLink + "/data", product).then(res => {
      cb(res);
    });
  },
  deleteProductApi: (id, cb) => {
    axios.delete(baseLink + "/data/" + id).then(res => {
      cb(res);
    });
  },
};
