import React, { useEffect, useState } from 'react';
import PropTypes from 'prop-types';
import { Dropdown } from 'semantic-ui-react';

const AssoSelector = function ({
  onChange = () => {},
  value = null,
  fluid = false,
  placeholder = 'Choisir une association',
}) {
  const [loading, setLoading] = useState(true);
  const [assosList, setAssosList] = useState([]);
  const [asso, setAsso] = useState(value);
  const assosListUrl = '/proxy_pda/get_assos_list';

  useEffect(() => {
    fetch(assosListUrl)
      .then((response) => {
        if (response.status === 200) {
          response.json().then((validResponse) => {
            const assosTmp = [];
            validResponse.results.map((asso) => {
              assosTmp.push({
                key: asso.id,
                value: asso.id,
                text: asso.shortname,
              });
            });
            setAssosList(assosTmp);
            setLoading(false);
          });
        } else {
          setLoading(false);
        }
      });
  }, []);

  const handleChange = (e, { v }) => {
    setAsso(v);
    onChange(v);
  };

  return (
    <Dropdown
      options={loading ? [] : assosList}
      placeholder={placeholder}
      loading={loading}
      value={asso}
      onChange={handleChange}
      selection
      deburr
      fluid={fluid}
    />
  );
};

AssoSelector.propTypes = {
  onChange: PropTypes.func,
  value: PropTypes.string,
  fluid: PropTypes.bool,
  placeholder: PropTypes.string,
};

export default AssoSelector;
