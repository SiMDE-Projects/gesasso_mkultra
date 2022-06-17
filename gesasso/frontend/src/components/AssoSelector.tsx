import React, { useEffect, useState } from 'react';
import PropTypes from 'prop-types';
import { Dropdown } from 'semantic-ui-react';

export interface IAssoSelectorProps {
  value: string;
  fluid: boolean;
  placeholder: string;

  onChange(value: string): void;
}

const AssoSelector = ({
  onChange,
  value,
  fluid,
  placeholder,
}: IAssoSelectorProps) => {
  const [loading, setLoading] = useState(true);
  const [assosList, setAssosList] = useState([]);
  const [asso, setAsso] = useState(value);
  const assosListUrl = `${process.env.GESASSO_BASE_URL}proxy_pda/get_assos_list`;

  useEffect(() => {
    fetch(assosListUrl)
      .then((response) => {
        if (response.status === 200) {
          response.json().then((validResponse) => {
            const assosTmp: React.SetStateAction<any[]> = [];
            validResponse.forEach((x: { id: string; shortname: string; }) => {
              assosTmp.push({
                key: x.id,
                value: x,
                text: x.shortname,
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

  const handleChange = (e, v) => {
    setAsso(v.value);
    onChange(v.value);
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

AssoSelector.defaultProps = {
  onChange: () => {
  },
  value: null,
  fluid: false,
  placeholder: 'Choisir une association',
};

export default AssoSelector;
