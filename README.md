<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Voucher Management API Docs</title>
  <style>
    body {
      font-family: "Segoe UI", sans-serif;
      background-color: #f9f9f9;
      color: #333;
      padding: 2rem;
      line-height: 1.6;
    }
    h1, h2, h3 {
      color: #2c3e50;
    }
    code, pre {
      background: #f4f4f4;
      border: 1px solid #ddd;
      padding: 10px;
      border-radius: 5px;
      display: block;
      white-space: pre-wrap;
      font-family: monospace;
    }
    table {
      width: 100%;
      border-collapse: collapse;
      margin: 1rem 0;
    }
    table th, table td {
      padding: 8px 12px;
      border: 1px solid #ccc;
      text-align: left;
    }
    table th {
      background-color: #e9ecef;
    }
    .section {
      margin-bottom: 2rem;
    }
  </style>
</head>
<body>

  <h1>📘 Voucher Management API</h1>

  <div class="section">
    <h2>🔗 Base URL</h2>
    <code>https://npnc11v0y5.execute-api.us-east-1.amazonaws.com/Prod</code>
  </div>

  <div class="section">
    <h2>📌 Overview</h2>
    <p>This API allows you to:</p>
    <ul>
      <li><strong>Create</strong> vouchers</li>
      <li><strong>Fetch</strong> vouchers</li>
      <li><strong>Validate</strong> voucher codes</li>
    </ul>
    <p>Use the query parameter <code>type</code> to specify the operation.</p>
  </div>

  <div class="section">
    <h2>🚀 Endpoint: <code>/vouchers</code></h2>
    <h3>Method: GET</h3>
    <table>
      <thead>
        <tr>
          <th>Parameter</th>
          <th>Type</th>
          <th>Required</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
        <tr><td>type</td><td>string</td><td>✅ Yes</td><td>Operation type: <code>create</code>, <code>get</code>, or <code>validate</code></td></tr>
        <tr><td>orgName</td><td>string</td><td>❌ No</td><td>Organization name (used in <code>create</code> and <code>get</code>)</td></tr>
        <tr><td>examName</td><td>string</td><td>❌ No</td><td>Exam name (used in <code>create</code> and <code>get</code>)</td></tr>
        <tr><td>discount</td><td>integer</td><td>❌ No</td><td>Discount percentage (used in <code>create</code>)</td></tr>
        <tr><td>expiryDate</td><td>string</td><td>❌ No</td><td>Expiry date in <code>MM-DD-YYYY</code> (used in <code>create</code>)</td></tr>
        <tr><td>nVouchers</td><td>integer</td><td>❌ No</td><td>Number of vouchers to generate (used in <code>create</code>)</td></tr>
        <tr><td>voucherId</td><td>string</td><td>❌ No</td><td>Voucher ID to validate (used in <code>validate</code>)</td></tr>
      </tbody>
    </table>
  </div>

  <div class="section">
    <h2>🧪 Example Requests</h2>

    <h3>Create Vouchers</h3>
    <pre><code>curl --location 'https://npnc11v0y5.execute-api.us-east-1.amazonaws.com/Prod/vouchers?type=create&amp;orgName=abc&amp;examName=test&amp;discount=10&amp;expiryDate=10-09-2025&amp;nVouchers=5'</code></pre>

    <h3>Fetch Vouchers</h3>
    <pre><code>curl --location 'https://npnc11v0y5.execute-api.us-east-1.amazonaws.com/Prod/vouchers?type=get&amp;orgName=abc&amp;examName=test'</code></pre>

    <h3>Validate Voucher</h3>
    <pre><code>curl --location 'https://npnc11v0y5.execute-api.us-east-1.amazonaws.com/Prod/vouchers?type=validate&amp;voucherId=9F6AA494'</code></pre>
  </div>

  <div class="section">
    <h2>📤 Responses</h2>
    <h3><code>200 OK</code></h3>
    <pre><code>{
  "message": "Operation completed successfully"
}</code></pre>

    <h3><code>400 Bad Request</code></h3>
    <p>Returned when required parameters are missing or invalid.</p>

    <h3><code>500 Internal Server Error</code></h3>
    <p>Returned when the server fails to process the request.</p>
  </div>

</body>
</html>
