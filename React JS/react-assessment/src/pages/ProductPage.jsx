import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import {
  fetchProducts,
  addProduct,
  deleteProduct,
  updateProduct,
} from "../redux/productSlice";

function ProductPage() {
  const dispatch = useDispatch();
  const { productList, loading } = useSelector((state) => state.products);

  const [search, setSearch] = useState("");
  const [editId, setEditId] = useState(null);

  const [formData, setFormData] = useState({
    productName: "",
    price: "",
    offerPrice: "",
    photo: "",
    qty: "",
    description: "",
    addedDate: "",
  });

  useEffect(() => {
    dispatch(fetchProducts());
  }, [dispatch]);

  const handleChange = (e) => {
    const { name, value, files } = e.target;

    if (name === "photo") {
      setFormData({
        ...formData,
        photo: files[0] ? URL.createObjectURL(files[0]) : "",
      });
    } else {
      setFormData({
        ...formData,
        [name]: value,
      });
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    if (
      !formData.productName ||
      !formData.price ||
      !formData.offerPrice ||
      !formData.qty ||
      !formData.description ||
      !formData.addedDate
    ) {
      alert("Please fill all fields");
      return;
    }

    if (editId) {
      dispatch(updateProduct({ id: editId, ...formData }));
      alert("Product updated successfully");
      setEditId(null);
    } else {
      dispatch(addProduct(formData));
      alert("Product added successfully");
    }

    setFormData({
      productName: "",
      price: "",
      offerPrice: "",
      photo: "",
      qty: "",
      description: "",
      addedDate: "",
    });
  };

  const handleDelete = (id) => {
    if (window.confirm("Are you sure you want to delete this product?")) {
      dispatch(deleteProduct(id));
    }
  };

  const handleEdit = (product) => {
    setEditId(product.id);
    setFormData(product);
    window.scrollTo({ top: 0, behavior: "smooth" });
  };

  const filteredProducts = productList.filter((product) =>
    product.productName.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <>
      <section className="bg-light py-5">
        <div className="container">
          <div className="row align-items-center">
            <div className="col-md-7">
              <h1 className="fw-bold display-5">
                Manage Products Easily
              </h1>
              <p className="lead">
                Add, update, delete and search products using React JS,
                Redux Toolkit and REST API.
              </p>
              <a href="#products" className="btn btn-dark px-4">
                View Products
              </a>
            </div>

            <div className="col-md-5 text-center">
              <div className="card shadow border-0">
                <div className="card-body p-4">
                  <h4 className="fw-bold">Assessment Features</h4>
                  <p className="mb-1">Redux Toolkit CRUD</p>
                  <p className="mb-1">API Integration</p>
                  <p className="mb-1">Search Filter</p>
                  <p className="mb-0">Bootstrap 5 UI</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section className="py-5">
        <div className="container">
          <div className="card shadow border-0">
            <div className="card-header bg-dark text-white">
              <h4 className="mb-0">
                {editId ? "Update Product" : "Add Product"}
              </h4>
            </div>

            <div className="card-body">
              <form onSubmit={handleSubmit}>
                <div className="row g-3">
                  <div className="col-md-6">
                    <label className="form-label">Product Name</label>
                    <input
                      type="text"
                      name="productName"
                      className="form-control"
                      value={formData.productName}
                      onChange={handleChange}
                    />
                  </div>

                  <div className="col-md-3">
                    <label className="form-label">Price</label>
                    <input
                      type="number"
                      name="price"
                      className="form-control"
                      value={formData.price}
                      onChange={handleChange}
                    />
                  </div>

                  <div className="col-md-3">
                    <label className="form-label">Offer Price</label>
                    <input
                      type="number"
                      name="offerPrice"
                      className="form-control"
                      value={formData.offerPrice}
                      onChange={handleChange}
                    />
                  </div>

                  <div className="col-md-4">
                    <label className="form-label">Photo</label>
                    <input
                      type="file"
                      name="photo"
                      className="form-control"
                      onChange={handleChange}
                    />
                  </div>

                  <div className="col-md-4">
                    <label className="form-label">Quantity</label>
                    <input
                      type="number"
                      name="qty"
                      className="form-control"
                      value={formData.qty}
                      onChange={handleChange}
                    />
                  </div>

                  <div className="col-md-4">
                    <label className="form-label">Added Date</label>
                    <input
                      type="date"
                      name="addedDate"
                      className="form-control"
                      value={formData.addedDate}
                      onChange={handleChange}
                    />
                  </div>

                  <div className="col-12">
                    <label className="form-label">Description</label>
                    <textarea
                      name="description"
                      className="form-control"
                      rows="3"
                      value={formData.description}
                      onChange={handleChange}
                    ></textarea>
                  </div>

                  <div className="col-12">
                    <button className="btn btn-dark px-4">
                      {editId ? "Update Product" : "Add Product"}
                    </button>

                    {editId && (
                      <button
                        type="button"
                        className="btn btn-secondary ms-2"
                        onClick={() => {
                          setEditId(null);
                          setFormData({
                            productName: "",
                            price: "",
                            offerPrice: "",
                            photo: "",
                            qty: "",
                            description: "",
                            addedDate: "",
                          });
                        }}
                      >
                        Cancel
                      </button>
                    )}
                  </div>
                </div>
              </form>
            </div>
          </div>
        </div>
      </section>

      <section className="py-5 bg-light" id="products">
        <div className="container">
          <div className="d-flex justify-content-between align-items-center mb-4">
            <h3 className="fw-bold mb-0">Product List</h3>

            <input
              type="text"
              className="form-control w-25"
              placeholder="Search product..."
              value={search}
              onChange={(e) => setSearch(e.target.value)}
            />
          </div>

          <div className="table-responsive">
            <table className="table table-bordered table-hover align-middle bg-white shadow-sm">
              <thead className="table-dark">
                <tr>
                  <th>Photo</th>
                  <th>Name</th>
                  <th>Price</th>
                  <th>Offer Price</th>
                  <th>Qty</th>
                  <th>Description</th>
                  <th>Added Date</th>
                  <th>Action</th>
                </tr>
              </thead>

              <tbody>
                {loading ? (
                  <tr>
                    <td colSpan="8" className="text-center">
                      Loading...
                    </td>
                  </tr>
                ) : filteredProducts.length > 0 ? (
                  filteredProducts.map((product) => (
                    <tr key={product.id}>
                      <td>
                        {product.photo ? (
                          <img
                            src={product.photo}
                            alt={product.productName}
                            width="70"
                            height="70"
                            className="rounded object-fit-cover"
                          />
                        ) : (
                          "No Image"
                        )}
                      </td>
                      <td>{product.productName}</td>
                      <td>₹{product.price}</td>
                      <td>₹{product.offerPrice}</td>
                      <td>{product.qty}</td>
                      <td>{product.description}</td>
                      <td>{product.addedDate}</td>
                      <td>
                        <button
                          className="btn btn-sm btn-warning me-2"
                          onClick={() => handleEdit(product)}
                        >
                          Edit
                        </button>

                        <button
                          className="btn btn-sm btn-danger"
                          onClick={() => handleDelete(product.id)}
                        >
                          Delete
                        </button>
                      </td>
                    </tr>
                  ))
                ) : (
                  <tr>
                    <td colSpan="8" className="text-center text-danger">
                      No records found
                    </td>
                  </tr>
                )}
              </tbody>
            </table>
          </div>
        </div>
      </section>
    </>
  );
}

export default ProductPage;