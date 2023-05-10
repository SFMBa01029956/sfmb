import { Container, Row, Col } from 'react-bootstrap';
import ReactDOM from 'react-dom';

import { MailchimpForm } from './MailchimpForm';
import logo from '../assets/img/logo.svg';
import navIcon1 from '../assets/img/nav-icon1.svg';
import { CQRCode } from './CQRCode';
import qr from '../assets/img/qr.png';

export const Footer = () => {
  const handleShareButtonClick = () => {
    const newWindow = window.open('', '_blank');
    // Add component to new window
    // ReactDOM.render(<CQRCode value={window.location.href} />, newWindow.document.body);
    ReactDOM.render(<img src={qr} alt="qr" />, newWindow.document.body);
  };

  return (
    <footer className="footer">
      <Container>
        <Row className="align-item-center">
          <MailchimpForm />
          <Col sm={6}>
            <img src={logo} alt="logo" />
          </Col>
          <Col sm={6} className="text-center text-sm-end">
            <div className="share-btn">
              <button onClick={handleShareButtonClick}>Share this page</button>
            </div>
            <div className="social-icon">
              <a
                href="https://www.linkedin.com/in/salvador-federico-milan%C3%A9s-braniff-160631238/"
                target="_blank"
                rel="noreferrer"
              >
                <img src={navIcon1} alt="" />
              </a>
            </div>
            <p>Salvador Federico Milanés Braniff &copy; All Rights Reserved</p>
          </Col>
        </Row>
      </Container>
    </footer>
  );
};