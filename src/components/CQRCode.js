import 'bootstrap/dist/css/bootstrap.min.css'

import QRCode from 'qrcode.react'

export const CQRCode = (value) => {
  return (
    <div>
      <QRCode value={value} />
    </div>
  );
};