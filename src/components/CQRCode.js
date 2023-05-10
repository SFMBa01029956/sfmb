import styles from './qr.css'
import 'bootstrap/dist/css/bootstrap.min.css'

import QRCode from 'qrcode.react'

export const CQRCode = (value) => {
  return (
    <div style={styles.div}>
      <QRCode value={value} />
    </div>
  );
};