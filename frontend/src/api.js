// 로컬
// const baseURL = "http://127.0.0.1:5000/";
// 배포
// const baseURL = process.env.VUE_APP_BACKEND_URL;
const baseURL =
  "https://port-0-kyobobook-review-python-flask-server-53px25lbux1h4i.gksl2.cloudtype.app/";
const get = async endPoint => {
  console.log("request URL", baseURL + endPoint);
  return await fetch(baseURL + endPoint);
};
const post = async (endPoint, data) => {
  console.log("data", JSON.stringify(data));
  return await fetch(baseURL + endPoint, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  });
};

export { get, post };
